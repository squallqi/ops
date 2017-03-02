#!/usr/bin/env python
#coding:utf-8
import os
import threading
from uuid import uuid1
from django.contrib import admin
from django.db import models
import salt.client
from django.forms import RadioSelect, forms
from mptt.admin import MPTTModelAdmin
from deploy_manager.models import *
from deploy_manager.admin import *

import salt.runner
import salt.config
import sys



@admin.register(ProjectModule)
class ProjectModuleAdmin(MPTTModelAdmin):
    list_display = ['name', 'parent', 'create_time', 'update_time']
    search_fields = ['name']
    list_filter = ['parent']


class ProjectVersionInline(admin.TabularInline):
    model = ProjectVersion
    fields = ['name', 'is_default', 'files']
    verbose_name = '版本'
    verbose_name_plural = '版本'
    extra = 0

    class Media:
        js = (
            '/static/js/ProjectVersionInline.js',
        )


class HostInline(admin.TabularInline):
    model = Project.host.through
    fields = ['host']
    verbose_name = '主机'
    verbose_name_plural = '主机'
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_module', 'name', 'job_script_type',
                    'create_time', 'update_time',
                    'deployMsg']
    search_fields = ['host']
    list_filter = ['job_script_type']
    inlines = [ProjectVersionInline, HostInline]

    actions = ['deploydefaultAction', ]

    def deployMsg(self, obj):
        try:
            return dict(DEPLOY_STATUS)[obj.projectversion_set.
                get(is_default=True).deployjob_set.
                order_by('-update_time').all()[0].deploy_status]
        except Exception as e:
            return ""

    deployMsg.short_description = '部署状态'

    # def save_formset(self, request, form, formset, change):
    #     instances = form.save(commit=False)
    #     formset.save()

    # 这里可以切换成自己的URL
    # def view_on_site(self, obj):
    #     url = reverse('person-detail', kwargs={'slug': obj.slug})
    #     return 'https://example.com' + url

    def deploydefaultAction(self, request, queryset):
        for obj in queryset:
            version = obj.projectversion_set.get(is_default=True)
            job = DeployJob(project_version=version, job_name='部署' + obj.name + ":" + version.name)
            job.save()
            thread = cmdThread(job)
            thread.start()
            self.message_user(request, "%s 个部署作业成功启动" % len(queryset))

    deploydefaultAction.short_description = "部署默认版本"


class DeployJobDetailInline(admin.StackedInline):
    model = DeployJobDetail
    fields = ['host', 'job_cmd', 'duration', 'deploy_message', 'stderr']
    verbose_name = '作业详情'
    verbose_name_plural = '作业详情'
    extra = 0
    can_delete = False
    readonly_fields = ['host', 'job_cmd', 'duration', 'deploy_message', 'stderr',
                       'create_time', 'update_time']
    ordering = ['-create_time']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class cmdThread(threading.Thread):
    def __init__(self, instances):
        threading.Thread.__init__(self)
        self.instances = instances

    def run(self):
        project = self.instances.project_version.project
        hosts = project.host.all()
        uid = uuid1().__str__()
        scriptPath = PACKAGE_PATH + uid + ".sls"
        output = open(scriptPath, 'w')
        defaultVersion = project.projectversion_set.get(is_default=True)
        playbookContent = project.playbook.replace('${version}', defaultVersion.name)
        output.write(playbookContent)
        output.close()

        target = ""
        for host in hosts:
            target = host.host_name + ","
        if target != "":
            target = target[0:len(target) - 1]
        result = None

        if project.job_script_type == 0:
            result = salt_api_token({'fun': 'state.sls', 'tgt': target,
                                     'arg': uid},
                                    SALT_REST_URL, {'X-Auth-Token': token_id()}).CmdRun()['return'][0]
        if project.job_script_type == 1:
            # 脚本类型的下个版本再支持
            pass

        for master in result:
            if isinstance(result[master], dict):
                for cmd in result[master]:
                    targetHost = Host.objects.get(host_name=master)
                    msg = ""
                    if "stdout" in result[master][cmd]['changes']:
                        msg = result[master][cmd]['changes']["stdout"]
                    stderr = ""
                    if "stderr" in result[master][cmd]['changes']:
                        stderr = result[master][cmd]['changes']["stderr"]
                    deployJobDetail = DeployJobDetail(
                        host=targetHost,
                        deploy_message=msg,
                        job=self.instances,
                        stderr=stderr,
                        job_cmd=result[master][cmd]['name'],
                        # start_time=result[master][cmd]['start_time'],
                        duration=result[master][cmd]['duration'],
                    )
                    deployJobDetail.save()

        os.remove(scriptPath)
        self.instances.deploy_status = 1
        self.instances.save()


@admin.register(DeployJob)
class DeployJobAdmin(admin.ModelAdmin):
    list_display = ['job_name', 'project_version', 'create_time', 'update_time', 'deploy_status']
    readonly_fields = ['job_name', 'project_version', 'deploy_status']
    search_fields = ['job_name']
    list_filter = ['deploy_status']
    inlines = [DeployJobDetailInline]

    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        js = ('/static/js/DeployJobAdmin.js',)

