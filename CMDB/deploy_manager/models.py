#!/usr/bin/env python
#coding:utf-8
from django.db import models
from django.utils.timezone import  now
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from CMDB.models import Host
from CMDB.settings import PACKAGE_PATH


class ProjectModule(MPTTModel):
    parent = TreeForeignKey('self', verbose_name='上级业务模块',
                            null=True, blank=True, related_name='children', db_index=True)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="业务模块名称")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class MPTTMeta:
        parent_attr = 'parent'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "业务模块"
        verbose_name_plural = verbose_name


JOB_SCRIPT_TYPE = (
    (0, 'sls'),
    (1, 'shell')
)


class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="业务名称")
    host = models.ManyToManyField(Host, default="", verbose_name="主机",
                                  blank=True, through='ProjectHost')
    project_module = models.ForeignKey(ProjectModule, verbose_name='业务模块', blank=True, null=True, default="")
    playbook = models.TextField(verbose_name='部署脚本', null=True, blank=True,
                                help_text='${version}代表默认版本号')
    job_script_type = models.IntegerField(default=0, choices=JOB_SCRIPT_TYPE,
                                          verbose_name='脚本语言')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "业务"
        verbose_name_plural = verbose_name


class ProjectVersion(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="版本名称")
    project = models.ForeignKey(Project, default="", verbose_name="业务名称", blank=True, null=True, )
    files = models.FileField(verbose_name='版本', blank=True, null=True, upload_to=PACKAGE_PATH + 'files')
    is_default = models.BooleanField(verbose_name='默认版本', blank=True, default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.project.__str__() + '---' + self.name

    class Meta:
        verbose_name = "版本信息"
        verbose_name_plural = verbose_name


class ProjectHost(models.Model):
    host = models.ForeignKey(Host, verbose_name='主机')
    project = models.ForeignKey(Project, verbose_name='业务')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.host.host_name

    class Meta:
        verbose_name = "业务主机"
        verbose_name_plural = verbose_name


DEPLOY_STATUS = (
    (0, '部署中'),
    (1, '部署完成'),
    (2, '部署失败'),
)


class DeployJob(models.Model):
    project_version = models.ForeignKey(ProjectVersion, verbose_name='版本')
    job_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="作业名称")
    deploy_status = models.IntegerField(null=True, blank=True, verbose_name="部署状态", choices=DEPLOY_STATUS,
                                        default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.job_name

    class Meta:
        verbose_name = "历史作业"
        verbose_name_plural = verbose_name


class DeployJobDetail(models.Model):
    host = models.ForeignKey(Host, verbose_name='主机名')
    deploy_message = models.TextField(verbose_name='作业信息', blank=True, null=True)
    job = models.ForeignKey(DeployJob, verbose_name='作业名称', blank=True, null=True)

    job_cmd = models.TextField(blank=True, null=True, verbose_name="作业命令")
    start_time = models.DateTimeField(verbose_name='开始时间', blank=True, null=True)
    duration = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='执行时长', blank=True, null=True)
    stderr = models.TextField(blank=True, null=True, verbose_name="其他信息")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return ""

    class Meta:
        verbose_name = "部署详情"
        verbose_name_plural = verbose_name
