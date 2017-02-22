#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from splinter.browser import Browser
from time import sleep
#traceback模块被用来跟踪异常返回信息
import traceback

# 设定用户名，密码
username = u"squallqi"
passwd = u"squallqi7"

# 起始地址的cookies值要自己去找, 下面两个分别是杭州, 达州。如何找，在参考文献里有简单的介绍
starts = u"%u6C99%u57CE%2CSCP"
ends = u"%u5317%u4EAC%2CBJP"

# 时间格式2016-02-01
dtime = u"2017-02-15"
# 车次，选择第几趟，0则从上之下依次点击
order =12

#设定乘客姓名
#pa = u"张*(学生)"

#设定网址
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

#登录网站
def login():
    b.find_by_text("登录").click()
    sleep(3)

#第17至20行代码用于自动登录，username是12306账号名，passwd是12306密码
    b.fill("loginUserDTO.user_name", username)
    sleep(1)
    b.fill("userDTO.password", passwd)
    sleep(1)

    print u"等待验证码，自行输入..."
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break
#购票
def huoche():
    global b
#使用splinter打开chrome浏览器
    b = Browser(driver_name="chrome")
#返回购票页面
    b.visit(ticket_url)
    while b.is_text_present(u"登录"):
        sleep(1)
        login()
        if b.url == initmy_url:
            break
    try:
        print u"购票页面..."
        # 跳回购票页面
        b.visit(ticket_url)

        # 加载查询信息
#我们的模拟登录中以上海为始发站，营口东为终点站，时间选定2017年1月13日
        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()
        sleep(2)

        count = 0
        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                b.find_by_text(u"订票助手").click()
#程序自动点击查询后，结果如下：
                count +=1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    b.find_by_text(u"预订")[order - 1].click()
#程序自动点击预订后，结果如下：
#哇啦！我们成功预订了春运车票！
                except:
                    print u"还没开始预订"
                    continue
        else:
            while b.url == ticket_url:
                a = b.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except:
                    print u"还没开始预订"
                    continue
        sleep(1)

#注意：可以通过修改sleep的参数来调整延时, 但延时不要太低, 防止被12306网站认为是刷票屏蔽掉.
#        b.find_by_text(pa)[0].click()

#如果你运气不好，程序会给出一个这样的信息：
        print  u"能做的都做了.....不再对浏览器进行任何操作"

#如果出现这样的信息，你也不要灰心，重新执行程序，让好运降临！

    except Exception as e:
        print(traceback.print_exc())
if __name__ == "__main__":
    huoche()
