#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''def outer(fun):
    def wrapper():
        print 'haha'
        print 'xixi'
        fun()
    return wrapper()
@outer
def fun1():
    print 'qiweiwei'
    '''


#fun1('qq')

#__init__
#__call__
class person:
    def __init__(self,name,gene,weight):
        self.name = name
        self.__Gene = gene #私有
        if name != 'qiweiwei':
            self.Gene = '男'
        self.weight = weight
        self.age = 18
    def talk(self):
        print 'you are beautiful'
    def fight(self,value):
        if self.weight > value:
            print 'da'
        else:
            print 'run'
p = person('qiweiwei','a',180)
p1 = person('squallqi','b',250)
p.age = 18
p.talk()
#p1.talk()
p1.fight(p.weight)

print p1.__dict__





