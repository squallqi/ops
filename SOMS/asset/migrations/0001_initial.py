# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 08:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaid', models.CharField(max_length=20, unique=True, verbose_name='\u533a\u57df\u4ee3\u7801')),
                ('area', models.CharField(max_length=50, verbose_name='\u533a\u53bf')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityid', models.CharField(max_length=20, unique=True, verbose_name='\u57ce\u5e02\u4ee3\u7801')),
                ('city', models.CharField(max_length=50, verbose_name='\u57ce\u5e02')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='IdcAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idc_name', models.CharField(max_length=20, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('idc_type', models.CharField(blank=True, max_length=20, verbose_name='\u673a\u623f\u7c7b\u578b')),
                ('idc_location', models.CharField(max_length=100, verbose_name='\u673a\u623f\u4f4d\u7f6e')),
                ('contract_date', models.CharField(max_length=30, verbose_name='\u5408\u540c\u65f6\u95f4')),
                ('idc_contacts', models.CharField(error_messages={'required': '\u8054\u7cfb\u7535\u8bdd\u4e0d\u80fd\u4e3a\u7a7a'}, max_length=30, validators=[django.core.validators.RegexValidator(code='\u53f7\u7801\u9519\u8bef', message='\u8bf7\u8f93\u5165\u6b63\u786e\u7684\u7535\u8bdd\u6216\u624b\u673a\u53f7\u7801', regex='^[^0]\\d{6,7}$|^[1]\\d{10}$')], verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('remark', models.TextField(blank=True, default='', max_length=255, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': 'IDC\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': 'IDC\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceid', models.CharField(max_length=20, unique=True, verbose_name='\u7701\u4efd\u4ee3\u7801')),
                ('province', models.CharField(max_length=50, verbose_name='\u7701\u4efd')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ServerAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodename', models.CharField(default=None, max_length=50, unique=True, verbose_name='Salt\u4e3b\u673a')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('manufacturer', models.CharField(blank=True, max_length=20, verbose_name='\u5382\u5546')),
                ('productname', models.CharField(blank=True, max_length=100, verbose_name='\u578b\u53f7')),
                ('sn', models.CharField(blank=True, max_length=20, verbose_name='\u5e8f\u5217\u53f7')),
                ('cpu_model', models.CharField(blank=True, max_length=100, verbose_name='CPU\u578b\u53f7')),
                ('cpu_nums', models.PositiveSmallIntegerField(verbose_name='CPU\u7ebf\u7a0b')),
                ('memory', models.CharField(max_length=20, verbose_name='\u5185\u5b58')),
                ('disk', models.TextField(blank=True, verbose_name='\u786c\u76d8')),
                ('network', models.TextField(blank=True, verbose_name='\u7f51\u7edc\u63a5\u53e3')),
                ('os', models.CharField(blank=True, max_length=200, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('virtual', models.CharField(blank=True, max_length=20, verbose_name='\u865a\u62df\u5316')),
                ('kernel', models.CharField(blank=True, max_length=200, verbose_name='\u5185\u6838')),
                ('shell', models.CharField(blank=True, max_length=10, verbose_name='Shell')),
                ('zmqversion', models.CharField(blank=True, max_length=10, verbose_name='ZeroMQ')),
                ('saltversion', models.CharField(blank=True, max_length=10, verbose_name='Salt\u7248\u672c')),
                ('locale', models.CharField(blank=True, max_length=200, verbose_name='\u7f16\u7801')),
                ('selinux', models.CharField(blank=True, max_length=50, verbose_name='Selinux')),
                ('idc', models.CharField(blank=True, max_length=50, verbose_name='\u673a\u623f')),
            ],
            options={
                'default_permissions': (),
                'verbose_name': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f',
                'verbose_name_plural': '\u4e3b\u673a\u8d44\u4ea7\u4fe1\u606f\u7ba1\u7406',
                'permissions': (('view_asset', '\u67e5\u770b\u8d44\u4ea7'), ('edit_asset', '\u7ba1\u7406\u8d44\u4ea7')),
            },
        ),
        migrations.AddField(
            model_name='cities',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='province_city_set', to='asset.Provinces', verbose_name='\u7701\u4efd'),
        ),
        migrations.AddField(
            model_name='areas',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_area_set', to='asset.Cities', verbose_name='\u57ce\u5e02'),
        ),
    ]
