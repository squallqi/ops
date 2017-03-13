#!/usr/bin/env python
#coding:utf-8
import os
from uuid import uuid1

import logging
import requests
from celery import task

from CMDB.models import Host, HostIP
from deploy_manager.models import DeployJobDetail
from saltjob.salt_https_api import salt_api_token
from saltjob.salt_token_id import token_id
#from ops.settings import PACKAGE_PATH,


@task(name='deployTask')
def deployTask(deployJob):
    logger = logging.getLogger(__name__)

    logger.info("动态生成脚本文件")
    project = deployJob.project_version.project
    defaultVersion = project.projectversion_set.get(is_default=True)

    hosts = project.host.all()

    uid = uuid1().__str__()
    logger.info("脚本UUID为:%s", uid)

    isSubScript = defaultVersion.sub_job_script_type == 100
    if isSubScript is True:
        if project.job_script_type == 0:
            logger.info("脚本类型为sls")
            scriptPath = PACKAGE_PATH + uid + ".sls"
        if project.job_script_type == 1:
            logger.info("脚本类型为sh")
            scriptPath = PACKAGE_PATH + uid + ".sh"
    else:
        if defaultVersion.sub_job_script_type == 0:
            logger.info("脚本类型为sls")
            scriptPath = PACKAGE_PATH + uid + ".sls"
        if defaultVersion.sub_job_script_type == 1:
            logger.info("脚本类型为sh")
            scriptPath = PACKAGE_PATH + uid + ".sh"

    output = open(scriptPath, 'w')

    logger.info("填写动态变量")

    if isSubScript is True:
        playbookContent = project.playbook
    else:
        playbookContent = defaultVersion.subplaybook

    playbookContent = playbookContent.replace('${version}', project.name)

    output.write(playbookContent)
    output.close()

    if SALT_CONN_TYPE == 'http':
        logger.info("当前执行模式为分离模式，发送脚本到Master节点")
        url = SALT_HTTP_URL + '/upload'
        files = {'file': open(scriptPath, 'rb')}
        requests.post(url, files=files)

    jobList = []

    for target in hosts:
        logger.info("执行脚本，目标主机为:%s", target)
        hasErr = False

        # SLS模式
        if project.job_script_type == 0:

            result = salt_api_token({'fun': 'state.sls', 'tgt': target,
                                     'arg': uid},
                                    SALT_REST_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]

            for master in result:
                if isinstance(result[master], dict):
                    for cmd in result[master]:

                        if not result[master][cmd]['result']:
                            hasErr = True

                        targetHost = Host.objects.get(host_name=master)
                        msg = ""
                        if "stdout" in result[master][cmd]['changes']:
                            msg = result[master][cmd]['changes']["stdout"]
                        stderr = ""
                        if "stderr" in result[master][cmd]['changes']:
                            stderr = result[master][cmd]['changes']["stderr"]

                        jobCmd = ""
                        if 'name' in result[master][cmd]:
                            jobCmd = result[master][cmd]['name']

                        duration = 0
                        if 'duration' in result[master][cmd]:
                            duration = result[master][cmd]['duration']

                        # startTime = None
                        # if 'start_time' in result[master][cmd]:
                        #     startTime = result[master][cmd]['start_time']
                        deployJobDetail = DeployJobDetail(
                            host=targetHost,
                            deploy_message=msg,
                            job=deployJob,
                            stderr=stderr,
                            job_cmd=jobCmd,
                            comment=result[master][cmd]['comment'],
                            is_success=result[master][cmd]['result'],
                            # start_time=startTime,
                            duration=duration,
                        )
                        jobList.append(deployJobDetail)

        if project.job_script_type == 1:
            result = salt_api_token({'fun': 'cmd.script', 'tgt': target,
                                     'arg': 'salt://%s.sh' % uid},
                                    SALT_REST_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
            for master in result:
                targetHost = Host.objects.get(host_name=master)
                if result[master]['stderr'] != '':
                    hasErr = True

                deployJobDetail = DeployJobDetail(
                    host=targetHost,
                    deploy_message=result[master]['stdout'],
                    job=deployJob,
                    stderr=result[master]['stderr'],
                    job_cmd=playbookContent,
                    is_success=True if result[master]['stderr'] == '' else False,
                )
                jobList.append(deployJobDetail)

    os.remove(scriptPath)
    deployJob.deploy_status = 1 if hasErr is False else 2
    deployJob.save()
    for i in jobList:
        i.save()
    logger.info("执行脚本完成")


@task(name='scanHostJob')
def scanHostJob():
    logger = logging.getLogger(__name__)
    logger.info("开始执行主机扫描操作")

    result = salt_api_token({'fun': 'grains.items', 'tgt': '*'},
                            SALT_REST_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]

    logger.info("扫描主机数量为[%s]", len(result))

    for host in result:
        try:
            rs = Host.objects.filter(host_name=host, host=result[host]["host"])
            if len(rs) == 0:
                logger.info("新增主机:%s", result[host]["host"])
                device = Host(host_name=host,
                              kernel=result[host]["kernel"],
                              kernel_release=result[host]["kernelrelease"],
                              virtual=result[host]["virtual"],
                              host=result[host]["host"],
                              osrelease=result[host]["osrelease"],
                              saltversion=result[host]["saltversion"],
                              osfinger=result[host]["osfinger"],
                              os_family=result[host]["os_family"],
                              num_gpus=int(result[host]["num_gpus"]),
                              system_serialnumber=result[host]["system_serialnumber"]
                              if 'system_serialnumber' in result[host] else result[host]["serialnumber"],
                              cpu_model=result[host]["cpu_model"],
                              productname=result[host]["productname"],
                              osarch=result[host]["osarch"],
                              cpuarch=result[host]["osarch"],
                              os=result[host]["os"],
                              # num_cpus=int(result[host]["num_cpus"]),
                              mem_total=int(result[host]["mem_total"]), )
                device.save()
                for ip in result[host]["ipv4"]:
                    hostip = HostIP(ip=ip, host=device)
                    hostip.save()
            else:
                entity = rs[0]
                logger.info("更新主机:%s", entity)
                # str = result[host]["num_cpus"]
                entity.kernel = result[host]["kernel"]
                # entity.num_cpus = str,
                entity.kernel_release = result[host]["kernelrelease"]
                entity.virtual = result[host]["virtual"]
                entity.osrelease = result[host]["osrelease"],
                entity.saltversion = result[host]["saltversion"]
                entity.osfinger = result[host]["osfinger"]
                entity.os_family = result[host]["os_family"]
                entity.num_gpus = int(result[host]["num_gpus"])
                entity.system_serialnumber = result[host]["system_serialnumber"] \
                    if 'system_serialnumber' in result[host] else result[host]["serialnumber"]
                entity.cpu_model = result[host]["cpu_model"]
                entity.productname = result[host]["productname"]
                entity.osarch = result[host]["osarch"]
                entity.cpuarch = result[host]["osarch"]
                entity.os = result[host]["os"]
                entity.mem_total = int(result[host]["mem_total"])

                entity.save()

                HostIP.objects.filter(host=entity).delete()
                for ip in result[host]["ipv4"]:
                    hostip = HostIP(ip=ip, host=entity)
                    hostip.save()

        except Exception as e:
            logger.error("自动扫描出现异常:%s", e)
