# -*- coding=utf:8 -*-

'''class person():
    xue = '血'
    def __init__(self,name):
        self.name = name
p1 = person('齐胜杰')
print p1.name'''


#类不能访问动态对象
#对象可以访问静态字段
class province:
    #静态字段
    memo = '中国的23个国家之一'
    def __init__(self,name,capital,leader):
    #动态字段
        self.name = name
        self.capital = capital
        self.leader = leader
    #动态方法
    def sports_meet(self):
        print self.capital +'能开运动会'
    #静态方法
    @staticmethod
    def foo():
        print '每个人都要hi起来'
    #特性
    @property
    def bar(self):
        print self.name
        return 'something'
hb = province('河北','石家庄','齐胜杰')
hl = province('张家口','沙城','齐胜杰')
#print hb.name,hb.memo
hb.name
hb.sports_meet()
province.foo()
hb.bar


import Mysql