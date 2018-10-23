# coding:utf-8
'''
@Created on :2018-10-14
@function:定义验证码类,生成图片验证码
@author: jxc
'''
import random
import os
import string
import json
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# 将随机函数赋给变量 rdint
rdint = random.randint

class vertifyCode():
    def __init__(self, width, height, bgColor, num, fontPath, fontSize, savePath):
        self.width = width  # 生成图片宽度
        self.height = height  # 生成图片高度
        self.bgColor = bgColor  # 生成图片背景颜色
        self.num = num  # 验证码字符个数
        self.fontPath = fontPath  # 字体路径
        self.fontSzie = fontSize  # 字体大小
        self.code = ''  # 验证内容
        self.img = Image.new(
            'RGB', (self.width, self.height), self.bgColor)  # 画布对象
        self.savePath = savePath  # 图片保存路径

    # 获取随机颜色，RGB格式
    def get_random_Color(self):
        c1 = rdint(50, 150)
        c2 = rdint(50, 150)
        c3 = rdint(50, 150)
        return (c1, c2, c3)

    # 随机生成1位字符,作为验证码内容
    def get_random_char(self):
        c = ''.join(random.sample(string.ascii_letters + string.digits, 1))
        self.code += c
        return c

    # 生成随机位置(x,y)
    def get_random_xy(self):
        x = rdint(0, int(self.width))
        y = rdint(0, int(self.height))
        return (x, y)

    # 根据字体文件生成字体，无字体文件则生成默认字体
    def get_font(self):
        if self.fontPath:
            if os.path.exists(self.fontPath):
                if self.fontSzie and self.fontSzie > 0 and self.fontSzie < self.height:
                    size = self.fontSzie
                else:
                    size = rdint(int(self.height / 1.5), int(self.height - 10))
                font = ImageFont.truetype(self.fontPath, size)
                return font
            raise Exception('字体文件不存在或路径错误', self.fontPath)
        return ImageFont.load_default().font

    # 图片旋转
    def rotate(self):
        deg = int(self.height / 3)  # 旋转角度
        self.img = self.img.rotate(rdint(0, deg), expand=0)

    # 画n条干扰线
    def drawLine(self, n):
        draw = ImageDraw.Draw(self.img)
        for i in range(n):
            draw.line([self.get_random_xy(), self.get_random_xy()],
                      self.get_random_Color())
        del draw

    # 画n个干扰点
    def drawPoint(self, n):
        draw = ImageDraw.Draw(self.img)
        for i in range(n):
            draw.point([self.get_random_xy()], self.get_random_Color())
        del draw

    # 写验证码内容
    def drawText(self, position, char, fillColor):
        draw = ImageDraw.Draw(self.img)
        draw.text(position, char, font=self.get_font(), fill=fillColor)
        del draw

    # 生成验证码图片，并返回图片对象
    def getVertifyImg(self):
        x_start = 2
        y_start = 0
        for i in range(self.num):
            x = x_start + i * int(self.width / (self.num))
            y = rdint(y_start, int(self.height / 3))
            self.drawText((x, y), self.get_random_char(),
                          self.get_random_Color())
        self.drawLine(3)
        self.drawPoint(60)
        return self.img

    # 将图片保存到内存,便于前台点击刷新
    # 将验证码保存到session中，返回内存中的图片数据
    def saveInMemory(self, request):
        img = self.getVertifyImg()
        request.session['code'] = self.code.lower()
        f = BytesIO()  # 开辟内存空间
        img.save(f, 'png')
        return f.getvalue()

    # 将图片保存在本地，并以json格式返回验证码内容
    def saveInLocal(self):
        img = self.getVertifyImg()
        try:
            img.save(self.savePath)
        except:
            raise NotADirectoryError('保存路径错误或不存在:' + self.savePath)
        return json.dumps({'code': self.code})
