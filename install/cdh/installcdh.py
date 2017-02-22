#!/usr/bin/env python
#coding:utf-8
#autor:Qiweiwei
import os
import time
import sys
def filename(*args):
	for file in args:
		if os.path.exists(file):
			print 'OK,%s is exists' %file
		else:
			print 'sorry you just need %s' %file
		  	sys.exit(0)
filename('/tmp/cm', '/tmp/cdh', '/tmp/cm/conf', 'my.cnf', 'ini.sql')


def install_base():
	try:
		os.system('apt-get install -y mysql-server')
		os.system('apt-get install -y apache2')
		os.system('sudo apt-get install -y  libmysql-java')
		os.system('service mysql stop')
		os.system('cp -rf /etc/mysql/my.cnf /etc/mysql/mysql.cnf.bak')
		os.system('cp -rf my.cnf /etc/mysql/')
		os.system('service mysql restart')
		os.system('mysql -uroot  < ini.sql')
		print 'install_mysql is finished'
	except Exception,e:
 		print 'install_mysql',e

def local_apt():
	try:
		#os.system('cp -rf distributions /tmp/cm/conf/')
		os.system('sudo apt-get install -y reprepro')
		os.system('cd /tmp;find /tmp/cm -name \*.deb -exec reprepro -Vb cm includedeb cloudera {} \;')
		os.system('sudo mv /tmp/cm /var/www/html')
		os.system('sudo chmod -R ugo+rX /var/www/html/cm')
		os.system('sudo mv /tmp/cdh /var/www/html')
		os.system('chmod -R ugo+rX /var/www/html/cdh')
		os.system('echo "APT::Get::AllowUnauthenticated "true";" > /etc/apt/apt.conf.d/myown')
		os.system('echo "vm.swappiness = 10" >> /etc/sysctl.conf')
		os.system('echo "deb http://10.1.10.175/cm cloudera contrib" >> /etc/apt/sources.list')
		os.system('echo "deb http://10.1.10.175/cm cloudera contrib" > /etc/apt/sources.list.d/my-private-cloudera-repo.list && apt-get update')
		#os.system('ssh 10.1.10.176  "echo "deb http://10.1.10.175/cm cloudera contrib" >> /etc/apt/sources.list"')
		#os.system('ssh 10.1.10.176 "echo "deb http://10.1.10.175/cm cloudera contrib" > /etc/apt/sources.list.d/my-private-cloudera-repo.list && apt-get update"')
		print 'Install local_apt is finished'
	except Exception,e:
 		print 'local_apt',e

def install_jdk():
 	try:
 		os.system('sudo apt-get purge openjdk*')
 		os.system('sudo apt-get install  oracle-j2sdk1.7')
 		print 'Intall_jdk is finished'
	except Exception,e:
 		print 'instal_jdk',e

def install_cdh():
	try:
		os.system('sudo apt-get autoremove --purge cloudera-manager-daemons cloudera-manager-server')
		os.system('sudo apt-get install   cloudera-manager-daemons cloudera-manager-server')
		os.system('/usr/share/cmf/schema/scm_prepare_database.sh -h localhost mysql cm cm 123456')
		os.system('sudo service cloudera-scm-server start')

	except Exception,e:
 		print 'install_cdh',e

if __name__=='__main__':
	install_base()
 	local_apt()
 	install_jdk()
 	install_cdh()
else:
	print 'install failed' 
