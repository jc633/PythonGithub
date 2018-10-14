# coding:utf-8
'''
@Created on :2018-10-14
@function:定义图片操作类
@author: jxc
'''
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
from CommonUtils.stringUtils import stringUtil

# 实例化操作类
stringutil = stringUtil()

class imgUtil():
    def __init__(self, imgDir, imgName):
        self.imgDir = dir
        self.imgName = imgName

    # 获取验证码图片
    def get_vertify_img(self):
        img = Image.new('RGB', (80, 34), (255, 255, 255))  # 创建画布实例
        font = ImageFont.load_default().font
# font = ImageFont.truetype("arial.TTF", random.randint(20, 23))  # 设置字体
        draw = ImageDraw.Draw(img, 'RGB')  # 创建画笔
        content = ''
        for i in range(5):
            #             draw.line(random.randint(0, 75), random.randint(0, 30), 40)
            fill = random.choice(stringutil.getRnStr(5))
            content += fill
            draw.text([5 + i * 12, 2], fill, font=font,
                      color=(random.randint(0, 70), random.randint(0, 100), random.randint(0, 150)))
        img.filter(ImageFilter.BLUR)  # 图片模糊
        img.save('/static/img/vertify.png')
        img.show()
