# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectversion',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=b'opsfiles', verbose_name=b'\xe7\x89\x88\xe6\x9c\xac'),
        ),
    ]
