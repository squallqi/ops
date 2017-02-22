#!/bin/bash
# Filename: bakfile.sh
# version 1.0
# author:Qiweiwei

# 要备份的数据库名，多个数据库用空格分开
databases=(goldhealth mysql k2bigdata goldwind)

# 要备份的软件名，多个数据库用空格分开
soft=(gold goldhealth k2bigdata)

# 备份文件要保存的目录
basepath='/data/backup/'

# 软件存放的目录
softpath='/opt/apache-tomcat8/webapps/'

if [ ! -d "$basepath" ]; then
  mkdir -p "$basepath"
fi
# 循环soft数组
for baksoft in ${soft[*]}
  do
  cd $softpath
  /bin/tar -zcvf $basepath$baksoft-$(date +%Y%m%d).tar.gz --exclude goldhealth/upload $baksoft
  done
# 循环databases数组
for db in ${databases[*]}
  do
    # 备份数据库生成SQL文件
    /usr/bin/mysqldump -uroot -proot --database $db > $basepath$db-$(date +%Y%m%d).sql
    
    # 将生成的SQL文件压缩
    tar zcvf $basepath$db-$(date +%Y%m%d).sql.tar.gz $basepath$db-$(date +%Y%m%d).sql
    
    # 删除7天之前的备份数据
    find $basepath -mtime +5 -name "*.tar.gz" -exec rm -rf {} \;
  done
# 删除生成的SQL文件
  rm -rf $basepath/*.sql