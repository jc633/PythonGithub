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
import hashlib

class stringUtil():
    # 获取随机的n位字符串
    def getRnStr(self, n):
        s = ''.join(random.sample(string.ascii_letters + string.digits, n))
        return s

    # 获取n位随机数字
    def getRnDigit(self, n):
        s = ''.join(random.sample(string.digits, n))
        return s

    # 获取当前时间并格式化 eg:2018-10-14 18:20
    def getDate(self):
        t = time.strftime('%Y-%m-%d  %H:%M', time.localtime())
        return t

    # 获取当前时间戳
    def getTimeStamp(self):
        return str(time.time())

    # 获取md5加密字符串
    def get_md5_string(self, value):
        if isinstance(value, str):
            m = hashlib.md5()
            m.update(value.encode('utf-8'))
            return m.hexdigest()
        raise TypeError('需要一个字符串,而不是:', value)

    # base64加密字符串
    def jiamiString(self, value):
        if value and isinstance(value, str):
            s = base64.b32encode(bytes(value, 'ascii')).decode()
            return s
        raise TypeError('所传值需为字符串,而不是:%s' % value)

    # base64解密字符串
    def jiemiString(self, value):
        if value:
            s = base64.b32decode(value).decode()
            return s
        raise TypeError('所传值为空:%s' % value)
