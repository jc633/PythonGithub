# coding:utf-8
'''
@Created on :2018-10-14
@function:定义图片操作类
@author: jxc
'''

from CommonUtils.stringUtils import stringUtil
import os
from PIL import Image
from GoodComputer import settings
# 实例化操作类
stringutil = stringUtil()

class imgUtil():
    def __init__(self, imgDir, imgName):
        self.imgDir = imgDir
        self.imgName = imgName
        self.imgPath = ''

    # 更改上传图片的图片名称
    # os.path.splitext(self.imgName)[1]获取图片后缀名
    def change_upImg_name(self, filename):
        newName = filename + os.path.splitext(self.imgName)[1]
        self.imgName = newName
        return newName

    # 图片缩放,scale_val:缩放比例
    def change_img_size(self, imgPth, scale_val):
        img = Image.open(imgPth)
        width, height = img.size  # 获取图片宽、高
        w = int(width * scale_val)
        h = int(height * scale_val)
        img = img.resize((w, h), Image.ANTIALIAS)
        img.save(imgPth)

    # 保存上传的图片
    def saveImg(self, upImg):
        img = Image.open(upImg)
        dir = settings.MEDIA_ROOT + self.imgDir  # 保存目录
        if not os.path.exists(dir):
            os.mkdir(dir)
        path = os.path.join(dir, self.imgName)  # 保存路径
        try:
            img.save(path)
            self.change_img_size(path, 0.5)
        except Exception as e:
            print(e)
