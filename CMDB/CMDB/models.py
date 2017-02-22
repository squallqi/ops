#!/usr/bin/env python
#coding:utf-8
from django.db import models
class UserInfo(models.Model):
    usename = models.CharField(max_length=50)
    passwd = models.CharField(max_length=15)
    memo = models.CharField(max_length=15)
class Group(models.Model):
    Name = models.CharField(max_length=50)
class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    group_relation = models.ManyToManyField('Group')
class Args(models.Model):
    name = models.CharField(max_length=20,null=True)
    not_name = models.CharField(max_length=20,null=False)
class Asset(models.Model):
    hostname = models.CharField(max_length=256)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
class UserInfo_Temp(models.Model):
    GENDER_CHOICE = (
        (u'1',u'普通用户'),
        (u'2',u'管理员'),
        (u'3',u'超级用户'),
    )
    UserType = models.CharField(max_length=2,choices=GENDER_CHOICE)
