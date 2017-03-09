#!/usr/bin/env python
#coding:utf-8
import sys
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'
#from __future__ import unicode_literals
from django.db import models



class ISP(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'名称')
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"ISP类型"
        verbose_name_plural = verbose_name


class IDCLevel(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'名称')
    comment = models.TextField(verbose_name=u'描述')
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机房等级"
        verbose_name_plural = verbose_name


class IDC(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'机房名称')
    bandwidth = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'机房带宽')
    phone = models.CharField(max_length=255, verbose_name=u'联系电话')
    linkman = models.CharField(max_length=255, null=True, verbose_name=u'联系人')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"机房地址")
    concat_email = models.EmailField(verbose_name=u'联系邮箱', blank=True, null=True, default="")
    network = models.TextField(blank=True, null=True, verbose_name=u"IP地址段")
    create_time = models.DateField(auto_now=True, verbose_name=u'创建时间')
    operator = models.ForeignKey(ISP, verbose_name=u'ISP类型')
    type = models.ForeignKey(IDCLevel, verbose_name=u'机房类型')
    comment = models.TextField(blank=True, null=True, verbose_name=u"备注")
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机房"
        verbose_name_plural = verbose_name


class Cabinet(models.Model):
    idc = models.ForeignKey(IDC, verbose_name=u'机房')
    name = models.CharField(max_length=30, unique=True, verbose_name=u"机柜编号")
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机柜"
        verbose_name_plural = verbose_name


class Rack(models.Model):
    cabinet = models.ForeignKey(Cabinet, verbose_name=u'机柜')
    name = models.CharField(max_length=30, unique=True, verbose_name=u"机架名称")
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"机架"
        verbose_name_plural = verbose_name

class Host(models.Model):
    host_name = models.CharField(max_length=255, blank=False, null=True, verbose_name=u"主机DNS名称")
    kernel = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"系统内核")
    kernel_release = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"系统内核版本")
    virtual = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"设备类型")
    host = models.CharField(max_length=255, blank=False, null=True, verbose_name=u"主机名")
    osrelease = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"操作系统版本")
    saltversion = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"Salt版本")
    osfinger = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"系统指纹")
    os_family = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"系统类型")
    num_gpus = models.IntegerField(blank=True, null=True, verbose_name=u"GPU数量")
    system_serialnumber = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"SN号")
    cpu_model = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"CPU型号")
    productname = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"产品名称")
    osarch = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"系统架构")
    cpuarch = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"CPU架构")
    os = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"操作系统")
    mem_total = models.IntegerField(blank=True, null=True, verbose_name=u"内存大小")
    num_cpus = models.IntegerField(blank=True, null=True, verbose_name=u"CPU数量")
    rack = models.ForeignKey(Rack, verbose_name=u'机架', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.host_name

    class Meta:
        verbose_name = u"主机"
        verbose_name_plural = verbose_name


class HostIP(models.Model):
    ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"IP地址")
    host = models.ForeignKey(Host, default="", verbose_name=u"主机", blank=True, null=True, )
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = u"主机IP"
        verbose_name_plural = verbose_name
