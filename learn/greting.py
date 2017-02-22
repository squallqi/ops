# -*— coding=utf:8 -*-
import itchat, time, re
from itchat.content import *

@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search(u'年', msg['Text']).span()
    if match:
      itchat.send((u'齐胜杰携全家祝您新春快乐,阖家欢乐,鸡年大吉!'), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    itchat.send((u'鸡年大吉'), msg['FromUserName'])

itchat.auto_login(enableCmdQR=2,hotReload=True)
#itchat.run(debug=True)
itchat.run()



