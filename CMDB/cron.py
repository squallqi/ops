<<<<<<< HEAD
#!/usr/bin/env python
#coding:utf-8
import salt.client
import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "ops.settings"})
import django
django.setup()


from CMDB.models import HostIP, Host
from saltjob.salt_https_api import salt_api_token
from saltjob.salt_token_id import token_id
from ops.settings import SALT_REST_URL



def scanHostJob():
    result = salt_api_token({'fun': 'grains.items', 'tgt': '*'},
                            SALT_REST_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
    for host in result:
        try:
            rs = Host.objects.filter(host_name=host, host=result[host]["host"])
            print rs
            if len(rs) == 0:
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
                              num_cpus=int(result[host]["num_cpus"]),
                              mem_total=int(result[host]["mem_total"]), )
                print device
                device.save()
                for ip in result[host]["ipv4"]:
                    hostip = HostIP(ip=ip, host=device)
                    hostip.save()
            else:
                entity = rs[0]
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

        except Exception, e:
            print e
if __name__ == "__main__":
    scanHostJob()
