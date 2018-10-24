# coding:utf-8
''' 
  function：对豆瓣电影top250的信息进行可视化处理
'''
import os
import xlrd
import jieba
import numpy as np
from pyecharts import Pie
import matplotlib.pyplot as plt
from collections import Counter
os.chdir(r'C:\Users\Administrator\Desktop')


# 豆瓣top250中各国所占比例分析
def top250_area():
    ws = getSheet('top250.xlsx')
    data = ''
    j = 0
    area = ws.col_values(2, start_rowx = 1)
    for i in area:
        data += i.replace(' ', '')
    jieba.add_word('中国大陆')  # 设置后，不对'中国大陆'进行再划分
    data = ' '.join(jieba.cut(data))
    cout = Counter(data.split(' '))
    cout.pop('\xa0')  # 删除键 '\xa0'
    print(cout)
    num = []
    cls = []
    for k in cout.keys():  # 取前二十的数据
        j += 1
        if j < 21:
            cls.append(k)
            num.append(cout[k])
        else:
            break
    name = ''  # 图表名称
    pie = Pie('豆瓣top250中地区前二十所占比例分析')
    pie.add(name, cls, num, is_label_show = True, legend_orient = 'vertical', legend_pos = 'right', radius = [28, 65])
    pie.show_config()
    pie.render()


# 获取excel表对象
def getSheet(path):
    wc = xlrd.open_workbook(path, 'r')
    ws = wc.sheet_by_index(0)
    return ws


if __name__ == '__main__':
    top250_area()
