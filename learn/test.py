#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import re
#re.findall()
#re.search() #all
'''res1 = search('\d+', 'qeqeradf54ad6fafafadasdfasdf') #all
res1 = re.match('\d+', 'qeqeradf54ad6fafafadasdfasdf') #@begin
print res1.group()
res1 = re.findall('\d+', 'qeqeradf54ad6fafafadasdfasdf')
print ','.join(res1)
res1 = re.compile('\d+')
print res1.findall('qeqeradf54ad6fafafadasdfasdf')
#分组
res1 = re.search('(\d+)\w*(\d+)', 'qeqeradf12354ad656fafafadasdf1234asdf')
print res1.group()
print res1.groups()
'''
#字符  \d 数字 \w下划线,字母,数字  \t 制表符  . 除了回车以外的任意字符
#次数  * 大于等于0  + 大于等于1 ? 0或者1 {m} 次数 {m,n}  出现m到n不包括n的次数

'''try:
    import mysql

except ImportError,e:
    print 1,e
except ArithmeticError,e:
    print 2,e
except Exception,e:
    print 3,e
    print '404'
else:
    print 'i am ok'
finally:
    print '无论异常与否都执行'
'''

while True:
    a = raw_input('plesse tell me what is your nane: ')
    if a == 'qiweiwei':
        print a,'is my wife'
        break
    elif a == 'Qzai':
        print a,'is my son'
        break
    else:
        print a,'sorry,you get wrong answer!'




import MySQLdb





