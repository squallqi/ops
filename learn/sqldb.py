import MySQLdb
# -*- coding:utf-8 -*-
conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='mysql')
cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
user = cur.execute('select host,user from user limit 2 ')
data = cur.fetchall()
cur.close()
conn.close()
print user
print data