#!/usr/bin/env python
#coding:utf-8
from threading import Thread
def foo(arg,v):
    print arg
print 'before'
t1 = Thread(target=foo,args=(1,11,))
t1.start()
print 'after'

from multiprocessing import Pool
import  time
def f(x):
    time.sleep(1)
    print x
    print x*x
if __name__ == '__main__':
    p = Pool(5)
    print (p.map(f.[1, 2, 3]))