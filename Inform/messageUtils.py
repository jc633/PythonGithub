# coding:utf-8
'''
@Created on :2018-11-10
@function:定义消息相关操作类
@author: jxc
'''
from CommonUtils.sqlUtils import sqlUtil
from CommonUtils.stringUtils import stringUtil
from Inform.models import Message, MessageText
from datetime import datetime
import time
from argparse import ArgumentTypeError


sql_msg = sqlUtil(Message)
sql_msgText = sqlUtil(MessageText)
stringutil = stringUtil()


class messageUtil():
    def __init__(self):
        self.sendId = ''  # 消息发送者id
        self.recieveId = None  # 消息接受者id
        self.replyed_mId = None  # 被回复的消息id
        self.mt = ''  # 消息内容实例

    # 发送消息
    def send_msg(self, msg):
        if isinstance(msg, dict):
            if self.save_messageText(msg) and self.save_message():
                return True
            return False
        raise ArgumentTypeError('需要一个字典参数')

    # 保存消息
    def save_message(self):
        m = Message()  # 消息实例
        m.messageId = 'm' + stringutil.getRnDigit(6)
        m.sendId = self.sendId
        m.recieveId = self.recieveId
        m.replyed_messageId = self.replyed_mId
        m.msgStatue = False
        m.messageText = self.mt
        if sql_msg.add(m):
            return True
        return False

    # 保存消息内容
    def save_messageText(self, msg):
        mt = MessageText()  # 消息内容实例
        mt.msgId = 'mt' + stringutil.getRnDigit(6)
        mt.msgContent = msg.get('content')
        mt.msgType = msg.get('type')
        mt.msgTime = stringutil.getTimeStamp()
        if sql_msgText.add(mt):
            self.mt = mt
            return True
        return False

    # 查询消息内容
    def queryMessageText(self, args, **kwargs):
        mt = sql_msgText.select(args, **kwargs)
        if mt:
            return mt
        return None

    # 查询消息
    def queryMessage(self, args, **kwargs):
        ms = sql_msg.select(args, **kwargs)
        if ms:
            return ms
        return None
