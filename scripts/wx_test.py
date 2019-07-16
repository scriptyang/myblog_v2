#coding: utf-8

import itchat

class _wxyy(object):

    def _init_login(self):
        itchat.auto_login(hotReload=True)
        print('微信号登陆成功，程序开始执行')
    #发送文本消息
    def send_txt(self):
        self._init_login()
        for friend in itchat.get_friends():

            itchat.send('Hello ',toUserName='%s'%friend['UserName'])
    #获取指定朋友的朋友圈信息
    def get_friends(self):
        self._init_login()
        for friend in itchat.get_friends():
            print(itchat.get_contact())

_wxyy().get_friends()