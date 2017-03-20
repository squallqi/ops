#coding:utf-8
from django.contrib import admin

# Register your models here.
from django.contrib import admin

from tools_manager.models import *


@admin.register(ToolsTypes)
class ToolsTypesAdmin(admin.ModelAdmin):
    list_display = ['name', 'script_count']
    search_fields = ['name']

    def script_count(self, obj):
        return obj.toolsscript_set.count()

        script_count.short_description = '工具数量'


@admin.register(ToolsScript)
class ToolsScriptAdmin(admin.ModelAdmin):
    list_display = ['tools_type', 'name', 'tool_run_type', 'comment']
    search_fields = ['name']
    list_filter = ['tools_type', 'tool_run_type']

    class Media:
        js = ('/static/js/ToolsScriptAdmin.js',)
