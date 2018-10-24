# coding:utf-8
'''
  function:分析每日票房前十的上映天数、排片比、实时票房之间的关系
'''
import os
import xlrd
import numpy as np
from pyecharts import Pie, Line, Page
import matplotlib.pyplot as plt
os.chdir(r'C:\Users\Administrator\Desktop')


# 获取上映天数，排片比、实时票房
def getData():
    dic = {}  # 电影名字典
    data = {}  # 每部电影的数据字典
    wc = xlrd.open_workbook('day.xlsx', 'r')
    ws = wc.sheet_by_index(0)
    name = ws.col_values(0, start_rowx = 1)  # 电影名
    pday = ws.col_values(1, start_rowx = 1)  # 每日票房
    ppian = ws.col_values(4, start_rowx = 1)  # 排片比
    days = ws.col_values(5, start_rowx = 1)  # 上映天数
    # 得到每部电影连续4天的每日票房，排片比，上映天数
    for n in name:
        dic[n] = 0  # 得到电影名字典
    for k in dic.keys():
        # 定义三个列表分别存储三列的数据
        pd = []  # 每日票房
        pp = []  # 排片比
        sy = []  # 上映天数
        for i in range(len(name)):
            if name[i] == k:
                pd.append(pday[i])
                pp.append(ppian[i] * 100)
                sy.append(days[i])
        data.setdefault(k, [pd, pp, sy])
    return data  # 返回包含所需数据的字典

    
 # 上映天数与排片比、实时票房线性关系
def draw():
    data = getData()
    page = Page()  # Page 类，同页面显示多张图
    yname = ['厕所英雄', '哆啦A梦：大雄的金银岛', '完美陌生人']
    for i in yname:
        days = data[i][2]
        pp = [str(n)[0:5] for n in data[i][1]]
        dp = [str(n / 10)[0:5] for n in data[i][0]]
        line = Line('5日票房分析', i, subtitle_color = 'red', subtitle_text_size = 15)
        line.add("排片比/百分", days, pp, is_label_show = True, label_pos = "bottom", label_text_color = 'blue', label_text_size = 16)
        line.add("每日票房/十万", days, dp, is_label_show = True, label_text_color = 'green', label_text_size = 16, xaxis_name = '上映天数/天')
        page.add(line)
    page.render()

    
if __name__ == '__main__':
    draw()
    
