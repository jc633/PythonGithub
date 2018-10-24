# coding:utf-8
'''
   function:对电影票房前500的电影信息进行可视化处理
'''
import os
import xlrd
import numpy as np
import matplotlib.pyplot as plt
import jieba
from pyecharts import Pie
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression as LRg
from xlrd.xldate import xldate_as_tuple  # 转换excle表中的日期
os.chdir(r'C:\Users\Administrator\Desktop')


# 从票房信息表中获取到电影的上映时间和对应的票房数据
def getData():
    data = []
    ws = getSheet('piao.xlsx')
    piao = ws.col_values(2, start_rowx = 1)  # 读取第二列整列数据(票房)，从第一行开始
    time = ws.col_values(5, start_rowx = 1)  # 读取第五列整列数据(上映时间)，从第一行开始
    y = [xldate_as_tuple(n, 0) for n in time]  # 将excel表中的日期存储格式转为元组,采用0模式，基于1900年转换
    p = [m for m in piao]
    for i in range(len(time)):
        y[i] = str(y[i][0]) + '.' + str(y[i][1])  # 得到年份和月份，组成 年.月
        data.append([y[i],p[i]])
    return data  # 返回电影日期与票房的组合列表


# 得到从小到大排序的字典
def getSort_dic():
    con = getData()
    data = {}
    y = []
    for d in con:
        data.setdefault(d[0], d[1])
    x = sorted(data.keys())
    for k in x:
        y.append(float(data[k]) / 10000)
    return x, y


# 设置X轴的值
def setX():
    text = []  # 显示的内容列表
    for j in range(8, 19):
        text.append('20' + str(j))
    text[0] = '2008'
    text[1] = '2009'
    return text


# 获取excel表对象
def getSheet(path):
    wc = xlrd.open_workbook(path, 'r')
    ws = wc.sheet_by_index(0)
    return ws


# 中国电影市场十年发展历程折线图
def draw_zhexian():
    x, y = getSort_dic()
    # 重新定义X轴刻度
    index = np.arange(0, 100, 7.2)  # 设X轴总长为100，隔7.2显示一个刻度
    text = setX()
    plt.title('中国电影市场十年发展历程分析')
    plt.xlabel('年份/年')
    plt.ylabel('票房/亿元')
    plt.xticks(index, text)
    plt.plot(x, y)
    plt.show()


# 评价人数与票房的线性分析
def remark_piao():
    ws = getSheet('remark.xlsx')
    piao = ws.col_values(1, start_rowx = 1)
    remark = ws.col_values(2, start_rowx = 1)
    for i in range(len(piao)):
        piao[i] = float(str(piao[i] / 10000)[0:5])
        remark[i] = float(str(float(remark[i]) / 10000)[0:4])
    x = [[n] for n in remark]
    y = [[n] for n in piao]
    print('原始数据:')
    print(x,)
    print(y)
    cls = LRg()
    cls.fit(x, y)
    res = cls.predict(x)
    print('预测结果:')
    print(res)
    print('相关性:', '%4.2f%%' % cls.intercept_)
    plt.title('评论人数与电影票房的线性分析')
    plt.xlabel('评论数/万人')
    plt.ylabel('票房/亿元')
    plt.plot(x, y, 'r.')
    plt.plot(x, res, 'g-')
    plt.show()


# 中国电影票房聚类分析散点图
def sandian():
    con = []
    x, y = getSort_dic()
    for i in range(len(x)):
        con.append([x[i], y[i]])
    cls = KMeans(n_clusters = 4)
    cls.fit(con)  # 训练
    res = cls.predict(con)  # 预测
    index = np.arange(0, 100, 7.5)
    text = setX()
    plt.scatter(x, y, c = res, marker = 'o', s = 30)
    plt.title('中国电影票房聚类分析')
    plt.xlabel('时间/年')
    plt.ylabel('票房/亿元')
    plt.xticks(index, text)
    plt.show()


# 高票房电影剧情类型饼状图
def type_pie():
    ws = getSheet('piao.xlsx')
    type = ws.col_values(3, start_rowx = 1)  # 读取第三列整列数据(剧情类型)，从第一行开始
    con = ''
    i = 0
    for t in type:
        con += t
    con = ' '.join(jieba.cut(con.replace('/', '')))
    count = Counter(con.split(' '))
    num = []
    cls = []
    for k in count.keys():  # 取前二十的数据
        i+=1
        if i < 21:
            cls.append(k)
            num.append(count[k])
        else:
            break
    name = ''  # 图表名称
    pie = Pie('高票房电影中剧情类型所占比例分析')
    pie.add(name, cls, num, is_label_show = True, legend_orient = 'vertical', legend_pos = 'right', radius = [28, 65], rosetype = 'area',)
    pie.show_config()
    pie.render()

    
if __name__ == '__main__':
    # draw_zhexian()
   # remark_piao()
    #sandian()
    type_pie()

