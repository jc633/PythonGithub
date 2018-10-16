# coding:utf-8
'''
@Created on :2018-10-14
@function:定义字符串操作类
@author: jxc
'''
import string
import random
import time
import base64

class stringUtil():
    # 获取随机的n位字符串
    def getRnStr(self, n):
        s = ''.join(random.sample(string.ascii_letters + string.digits, n))
        return s

    # 获取当前时间并格式化 eg:2018-10-14 18:20
    def getDate(self):
        t = time.strftime('%Y-%m-%d   %H:%M', time.localtime())
        return t

    # base64加密字符串
    def jiamiString(self, value):
        if value:
            s = base64.b32encode(bytes(value, 'ascii')).decode()
            return s
        raise TypeError('所传值为空:%s' % value)

    # base64解密字符串
    def jiemiString(self, value):
        if value:
            s = base64.b32decode(value).decode()
            return s
        raise TypeError('所传值为空:%s' % value)
