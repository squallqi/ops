#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render
from django.http.response import HttpResponse
def index(request):
    return HttpResponse('hello index')
def login(request):
    return HttpResponse('hello login')
def list(request,id):
    print id
    return HttpResponse('hello list')
def Add(request,name):
    Asset.objects.create(hostname=name)
    return HttpResponse('ok')


