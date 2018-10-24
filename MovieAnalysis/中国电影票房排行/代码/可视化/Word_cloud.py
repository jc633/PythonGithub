# coding:utf-8
'''
   function:对文本文件进行可视化处理，得到其词云图或简单柱状图
'''
import os
from wordcloud import WordCloud
from collections import Counter
import re
from pyecharts import Bar
import matplotlib.pylab as plt
os.chdir(r'C:\Users\Administrator\Desktop')


# 得到词频字典
def getCounts(text):
    con = text.strip().replace('  ', ' ')
    regx = re.findall('[a-zA-Z#-\;]', con)
    for r in regx:
         con = con.replace(r, '')
#     with open('Actor_dealed.txt', 'w')as f1:
#         f1.write(con)
    with open('Company_dealed.txt', 'w')as f1:
           f1.write(con)
    count = Counter(con.split(' '))
    count.pop('')
    return count


# 票房前200电影的参与公司中词频前10的柱状图
def draw_zhu(text):
    i = 0
    num = []
    key = []
    counts = getCounts(text)
    num = sorted(counts.values(), reverse = True)[0:10]  # sorted对字典根据键值大小从大到小排序，reverse:反转
    # 根据键值找到对应的键
    for n in num:
        for k in counts.keys():
            if counts[k] == n and k[0:4] not in key:
                key.append(k[0:4])
    bar = Bar('中国高票房电影参与公司分析')
    bar.add('参与次数', key, num, is_label_show = True)
    bar.render()


# 画词云图
def draw_cloud(text):
   counts = getCounts(text)
   img = plt.imread('3.jpg')
   wc = WordCloud(background_color = 'white', mask = img).generate_from_frequencies(counts, 60)
   plt.imshow(wc, interpolation = 'bilinear')
#    plt.title('中国电影票房排行前200中的高流量演员分析')
   plt.title('中国电影票房排行前200中参与公司分析')
   plt.axis('off')
   plt.show()


# 取得文本文件中的数据
def getData_from_txt(path):
    with open(path, 'r')as f:
        text = f.read()
    return text


if __name__ == '__main__':
    path1 = 'Actor.txt'  # 主演txt文件
    path2 = 'Company.txt'  # 参与公司的txt文件
#     draw_cloud(getData_from_txt(path1))
    draw_zhu(getData_from_txt(path2))

