# coding:utf-8
'''
@Created on :2018-10-14
@function:定义图片操作类
@author: jxc
'''

from CommonUtils.stringUtils import stringUtil
import os

# 实例化操作类
stringutil = stringUtil()

class imgUtil():
    def __init__(self, imgDir, imgName):
        self.imgDir = dir
        self.imgName = imgName

    # 更改上传图片的图片名称
    # os.path.splitext(self.imgName)[1]获取图片后缀名
    def change_upImg_name(self, filename):
        newName = filename + os.path.splitext(self.imgName)[1]
        return newName
