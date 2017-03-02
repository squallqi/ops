# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CMDB', '0005_auto_20170301_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0')),
                ('deploy_status', models.IntegerField(blank=True, choices=[(0, b'\xe9\x83\xa8\xe7\xbd\xb2\xe4\xb8\xad'), (1, b'\xe9\x83\xa8\xe7\xbd\xb2\xe5\xae\x8c\xe6\x88\x90'), (2, b'\xe9\x83\xa8\xe7\xbd\xb2\xe5\xa4\xb1\xe8\xb4\xa5')], default=0, null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe7\x8a\xb6\xe6\x80\x81')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5386\u53f2\u4f5c\u4e1a',
                'verbose_name_plural': '\u5386\u53f2\u4f5c\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='DeployJobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy_message', models.TextField(blank=True, null=True, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe4\xbf\xa1\xe6\x81\xaf')),
                ('job_cmd', models.TextField(blank=True, null=True, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe5\x91\xbd\xe4\xbb\xa4')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('duration', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe6\x97\xb6\xe9\x95\xbf')),
                ('stderr', models.TextField(blank=True, null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe4\xbf\xa1\xe6\x81\xaf')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMDB.Host', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.DeployJob', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u90e8\u7f72\u8be6\u60c5',
                'verbose_name_plural': '\u90e8\u7f72\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('playbook', models.TextField(blank=True, help_text=b'${version}\xe4\xbb\xa3\xe8\xa1\xa8\xe9\xbb\x98\xe8\xae\xa4\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7', null=True, verbose_name=b'\xe9\x83\xa8\xe7\xbd\xb2\xe8\x84\x9a\xe6\x9c\xac')),
                ('job_script_type', models.IntegerField(choices=[(0, b'sls'), (1, b'shell')], default=0, verbose_name=b'\xe8\x84\x9a\xe6\x9c\xac\xe8\xaf\xad\xe8\xa8\x80')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1',
                'verbose_name_plural': '\u4e1a\u52a1',
            },
        ),
        migrations.CreateModel(
            name='ProjectHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMDB.Host', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.Project', verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u4e3b\u673a',
                'verbose_name_plural': '\u4e1a\u52a1\u4e3b\u673a',
            },
        ),
        migrations.CreateModel(
            name='ProjectModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe6\xa8\xa1\xe5\x9d\x97\xe5\x90\x8d\xe7\xa7\xb0')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='deploy_manager.ProjectModule', verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe4\xb8\x9a\xe5\x8a\xa1\xe6\xa8\xa1\xe5\x9d\x97')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u6a21\u5757',
                'verbose_name_plural': '\u4e1a\u52a1\u6a21\u5757',
            },
        ),
        migrations.CreateModel(
            name='ProjectVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe5\x90\x8d\xe7\xa7\xb0')),
                ('files', models.FileField(blank=True, null=True, upload_to=b'CMDBfiles', verbose_name=b'\xe7\x89\x88\xe6\x9c\xac')),
                ('is_default', models.BooleanField(default=False, verbose_name=b'\xe9\xbb\x98\xe8\xae\xa4\xe7\x89\x88\xe6\x9c\xac')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('project', models.ForeignKey(blank=True, default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.Project', verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u7248\u672c\u4fe1\u606f',
                'verbose_name_plural': '\u7248\u672c\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='host',
            field=models.ManyToManyField(blank=True, default=b'', through='deploy_manager.ProjectHost', to='CMDB.Host', verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_module',
            field=models.ForeignKey(blank=True, default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectModule', verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe6\xa8\xa1\xe5\x9d\x97'),
        ),
        migrations.AddField(
            model_name='deployjob',
            name='project_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deploy_manager.ProjectVersion', verbose_name=b'\xe7\x89\x88\xe6\x9c\xac'),
        ),
    ]
