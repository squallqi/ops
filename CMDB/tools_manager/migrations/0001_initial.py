# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolsParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=255, verbose_name='\u53c2\u6570\u540d\u79f0')),
                ('tool_value', models.CharField(max_length=255, verbose_name='\u53c2\u6570\u503c')),
            ],
            options={
                'verbose_name': '\u5de5\u5177\u53c2\u6570',
                'verbose_name_plural': '\u5de5\u5177\u53c2\u6570',
            },
        ),
        migrations.CreateModel(
            name='ToolsScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u5de5\u5177\u540d\u79f0')),
                ('tool_script', models.TextField(verbose_name='\u811a\u672c')),
                ('tool_run_type', models.IntegerField(choices=[(0, 'Salt\u811a\u672c'), (1, 'Shell\u811a\u672c')], default=0, verbose_name='\u811a\u672c\u7c7b\u578b')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='\u5de5\u5177\u8bf4\u660e')),
            ],
            options={
                'verbose_name': '\u5de5\u5177',
                'verbose_name_plural': '\u5de5\u5177',
            },
        ),
        migrations.CreateModel(
            name='ToolsTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u7c7b\u578b\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5de5\u5177\u7c7b\u578b',
                'verbose_name_plural': '\u5de5\u5177\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='toolsscript',
            name='tools_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsTypes', verbose_name='\u5de5\u5177\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='toolsparam',
            name='tool_script',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsScript', verbose_name='\u5de5\u5177'),
        ),
    ]