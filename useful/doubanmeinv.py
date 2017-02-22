# -*- coding: utf-8 -*-
import os 
import urllib2,urllib  
import re
info = u'''
-------------------------
0.所有
2.大胸妹
3.美腿控
4.有颜值
5.大杂烩
6.小翘臀
7.黑丝袜

请输入数字选择要下载的类别：
--------------------------
'''
print(info)
num = raw_input()  #获取下载选项
choices = {
    '0':r'0',
    '2':r'2',
    '3':r'3',
    '4':r'4',
    '5':r'5',
    '6':r'6',
    '7':r'7'
    }
choice = choices[num]
base_url = r'http://www.dbmeinv.com/dbgroup/show.htm'
title_index = r'?cid='
page_index = r'&pager_offset='

choice_url = base_url  + title_index + choice #要下载的页面的首页url

print(u'请输入起始页数：')
startpage = input() 
print(u'请输入结束页数：')
endpage = input()

url_pages = []  #储存所有要下载的url
#拼接url的各个部分
for index in range(startpage, endpage + 1):
    url_pages.append(choice_url + page_index + str(index))
#print(u'请输入要保存图片的绝对路径：')  
dir_path = '/opt/spider/pic/'  #保存路径名
#print(u'请输入要保存图片的文件夹名称：')  
dir_title = num #保存文件夹名
new_path = os.path.join(dir_path, dir_title)  #拼接出最终的路径
if not os.path.isdir(new_path):  #如果不存在就创建文件夹
    os.makedirs(new_path)
    print(u'将把图片保存在：%s' % new_path)
#开始下载该页面所有的图片
j = startpage  #用来给图片编号
for page in url_pages:  #循环每个要下载的页面
    myUrl = page  #取出一个url
    content = urllib2.urlopen(myUrl).read().decode('utf-8')  #获取url的html代码
    pattern = re.compile(r'<img.*?class=".*?_min".*?src="(.*?)".*?alt=.*?>'\
                         ,re.S)  #正则表达式对象
    allurl = re.findall(pattern, content)  #找到并返回所有符合对象的值，即图片链接
    i = 0  #编号用
    for item in allurl: 
        location = r'%s/%s_%s.jpg' % (new_path, j, i)  #图片存储路径

        urllib.urlretrieve(item, location)  #下载图片到指定位置
        i += 1
    j += 1