#!/usr/bin/env python
#coding:utf-8
import urllib2
def download(url, number_retries=2):
    print 'downing' url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'downing unkown',e.reason
        html = None
        if number_retries > 2:

