#!/usr/bin/env python
#coding:utf-8
import paramiko
import ConfigParser
import os
import datetime
#from ConfigParser import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read('config.ini')
#master = ''.join(cf.get('Host', 'master'))
#address = master.split(',')
#print  address

username = cf.get('Host','username')
password = cf.get('Host','password')
port = cf.getint('Host','port')
host = {
    'master': cf.get('Host','master'),
    'as': cf.get('Host', 'as'),
    #'batch1': cf.get('Host', 'batch1'),
    #'stream': cf.get('Host', 'stream')
}
if __name__=='__main__':
    for i in host.keys():
        hostname = i
        address = host[i]
        print address
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(address, port, username, password, look_for_keys=False)
            #paramiko.util.log_to_file("filename.log")
            stdin, stdout, stderr = client.exec_command('echo %s > /etc/hostname|hostname %s' % (hostname,hostname))
            #stdin, stdout, stderr = client.exec_command('hostname %s' % hostname)

            print stdout.read(),
        except Exception, e:
            print e
        client.close()