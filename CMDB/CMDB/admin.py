#!/usr/bin/env python
#coding:utf-8
import requests
from django.contrib import admin
from django.shortcuts import redirect
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from CMDB.admin import *
from CMDB.models import *
# #from deploy_manager.models import *
# from saltjob.salt_https_api import salt_api_token
# from saltjob.salt_token_id import token_id
# from saltjob.tasks import scanHostJob
# from saltops.settings import SALT_CONN_TYPE, SALT_HTTP_URL, SALT_REST_URL

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ['host_name', 'kernel', 'kernel_release',
                    'host', 'rack', 'saltversion', 'num_gpus', 'system_serialnumber', 'cpu_model',
                    'os', 'mem_total', 'cpuarch', 'osarch', 'create_time', 'update_time']
    search_fields = ['host']
    #inlines = [IPInline, ProjectInline]
    # fieldsets = (
    #     ('基础信息', {
    #         'fields': ('host_name', 'kernel', 'kernel_release','virtual',
    #                    'host','osrelease','osfinger','os_family','num_gpus','system_serialnumber')
    #     }),
    #     ('Agent信息', {
    #         'fields': ('saltversion',)
    #     }),
    # )


class RackInline(NestedStackedInline):
    model = Rack
    fields = ['name']
    verbose_name = '机架'
    verbose_name_plural = '机架'
    extra = 0
    fk_name = 'cabinet'



@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ['idc', 'name', 'rack_count', 'create_time', 'update_time']
    search_fields = ['name']
    fk_name = 'cabinet'

    def rack_count(self, obj):
        return obj.rack_set.count()

    rack_count.short_description = '机架数量'
    inlines = [RackInline]


class CabinetInline(NestedStackedInline):
    model = Cabinet
    fields = ['name']
    verbose_name = '机柜'
    verbose_name_plural = '机柜'
    extra = 0
    fk_name = 'idc'
    inlines = [RackInline]


@admin.register(IDC)
class IDCAdmin(NestedModelAdmin):
     list_display = ['name', 'type', 'phone',
                     'linkman', 'address',
                     'operator', 'concat_email', 'idc_count', 'create_time', 'update_time']
     search_fields = ['name']
     inlines = [CabinetInline]

     def idc_count(self, obj):
         return obj.cabinet_set.count()

     idc_count.short_description = '机柜数量'


@admin.register(IDCLevel)
class IDCLevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'create_time', 'update_time']
    search_fields = ['name', 'comment']


@admin.register(ISP)
class ISPAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'update_time']
    search_fields = ['name']


@admin.register(Rack)
class RackAdmin(admin.ModelAdmin):
    list_display = ['cabinet', 'name', 'create_time', 'update_time']
    search_fields = ['cabinet', 'name']

