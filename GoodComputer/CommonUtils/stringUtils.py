# coding:utf-8
'''
@Created on :2018-10-14
@function:定义字符串操作类
@author: jxc
'''
import string
import random

class stringUtil():
    # 获取随机的n位字符串
    def getRnStr(self, n):
        s = ''.join(random.sample(string.ascii_letters + string.digits, n))
        return s