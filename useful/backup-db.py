#!/usr/bin/env python
#-*- coding: UTF-8 -*- 
# Filename: mysqlbackup.py
# version 1.0
# author:Qiweiwei
import    os
import    time
import    sys
import    datetime
from stat import *
from ftplib import FTP
def writeLogs(filename,contents):
    f=file(filename,'aw')
    f.write(contents)
    f.close()
# mysql user
User = 'root'
 
# mysql password
Passwd = 'root'
 
# mysqldump command
Mysqlcommand = '/usr/bin/mysqldump'
 
# gzip command
Gzipcommand = '/bin/gzip'
 
# you want backup mysql database
Mysqldata  = ['goldhealth', 'mysql', 'k2bigdata','goldwind']
 
# you want    backup to dir
Tobackup = '/data/backup/'
logs_path=Tobackup + time.strftime('%Y-%m-%d')+'.log'
#backfilename = Tobackup + Mysqldata + '-' + time.strftime('%Y-%m-%d')+'.gz' 
for DB in Mysqldata:
# backup file name
  #print DB
  Backfile = Tobackup + DB + '-' + time.strftime('%Y-%m-%d') + '.sql'
# gzip file name
  Gzfile = Backfile +'.gz'
  if os.path.isfile(Gzfile):
    print Gzfile + " is already backup"
  else:
# backup  command
    Back_command = Mysqlcommand + ' -u' + User + ' -p' + Passwd + ' -P3306 ' + DB + ' > ' + Backfile
    if os.system(Back_command)==0:
      print 'Successful backup to', DB + ' to ' + Backfile
    else:
      print 'Backup FAILED'
# gzip command
  Gzip_command = Gzipcommand + ' ' + Backfile
  if os.system(Gzip_command)==0:
    writeLogs(logs_path,'Successful Gzip to' + Gzfile +'\n')
  else:
    writeLogs(logs_path,'database backup failed!+n')
# Delete back file
# show file list
filelist=[]
filelist=os.listdir(Tobackup)
# delete Gzfile 5 days ago
for i in range(len(filelist)):
                ft=time.gmtime(os.stat(Tobackup+filelist[i])[ST_MTIME])
                ftl=time.strftime('%Y-%m-%d',ft)
                year,month,day=ftl.split('-')
                ftll=datetime.datetime(int(year),int(month),int(day))

                localt=time.gmtime()
                localtl=time.strftime('%Y-%m-%d',localt)
                year,month,day=localtl.split('-')
                localtll=datetime.datetime(int(year),int(month),int(day))
                days=(localtll-ftll).days

                if days >5:
                                try:
                                                os.remove(Tobackup+filelist[i])
                                                print 'delete is ok'
                                except:
                                                log=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"    remove "+Tobackup+filelist[i]+"    fail \n"
                                                print log
########### FTP upload#####################
## upload ftp server
ftp=FTP()

ftp.set_debuglevel(2)
ftp.connect('10.12.100.45','21')
ftp.login('k2data','123456')

path = '/data/backup/'
backupfile = os.listdir('/data/backup/')
for  i in backupfile:
   print  i
   backfilename = path + i 
   print backfilename


#ftp.cwd()
   bufsize = 1024
   file_handler = open(backfilename,'rb')
   print file_handler
   ftp.storbinary('STOR %s' % os.path.basename(backfilename),file_handler,bufsize)
   file_handler.close()
ftp.quit()






#!/bin/bash

# 要备份的数据库名，多个数据库用空格分开
databases=(goldhealth mysql k2bigdata goldwind)
softpath=/opt/apache-tomcat8/webapps
soft=(gold goldwind k2bigdata)

# 备份文件要保存的目录
basepath='/data/backup'

if [ ! -d "$basepath" ]; then
  mkdir -p "$basepath"
fi
# 循环soft数组
for baksoft in ${soft[*]}
  do
  cd $softpath
  /bin/tar -zcvf $basepath$baksoft-$(date +%Y%m%d).tar.gz --exclude goldhealth/upload $baksoft

# 循环databases数组
for db in ${databases[*]}
  do
    # 备份数据库生成SQL文件
    /usr/bin/mysqldump -uUSER -pPASSWORD --database $db > $basepath$db-$(date +%Y%m%d).sql
    
    # 将生成的SQL文件压缩
    tar zcvf $basepath$db-$(date +%Y%m%d).sql.tar.gz $basepath$db-$(date +%Y%m%d).sql
    
    # 删除7天之前的备份数据
    find $basepath -mtime +7 -name "*.tar.gz" -exec rm -rf {} \;
  done