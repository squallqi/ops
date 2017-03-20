#coding:utf-8


from __future__ import unicode_literals


# Create your models here.
from django.db import models


class ToolsTypes(models.Model):
    name = models.CharField(max_length=255, verbose_name='类型名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工具类型"
        verbose_name_plural = verbose_name


TOOL_RUN_TYPE = (
    (0, 'Salt脚本'),
    (1, 'Shell脚本')
)


class ToolsScript(models.Model):
    name = models.CharField(max_length=255, verbose_name='工具名称')
    tool_script = models.TextField(verbose_name='脚本')
    tools_type = models.ForeignKey(ToolsTypes, verbose_name='工具类型')
    tool_run_type = models.IntegerField(verbose_name='脚本类型', choices=(TOOL_RUN_TYPE), default=0)
    comment = models.TextField(verbose_name='工具说明', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工具"
        verbose_name_plural = verbose_name


class ToolsParam(models.Model):
    tool_name = models.CharField(max_length=255, verbose_name='参数名称')
    tool_value = models.CharField(max_length=255, verbose_name='参数值')
    tool_script = models.ForeignKey(ToolsScript, verbose_name='工具')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "工具参数"
        verbose_name_plural = verbose_name
