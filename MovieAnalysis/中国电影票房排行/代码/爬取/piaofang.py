# coding:utf-8
'''
  function:获取中国电影网影库中票房排行前200的电影信息
'''
import requests
from bs4 import BeautifulSoup as bs
import os
import lxml
import re
import json
import csv
from openpyxl import workbook

os.chdir(r'C:\Users\Administrator\Desktop')

def getHtml(src):
    html = requests.get(src).content.decode('utf-8')
    for con in json.loads(html)['pData']:
        url = 'http://www.cbooo.cn/m/' + str(con['ID'])
        newhtml = requests.get(url).content.decode('utf-8')
        getInfor(newhtml)
        

def getInfor(html):
    # 获取电影基本信息并写入到piao.csv文件
    global j
    j += 1
    soup = bs(html, "lxml")
    basic_cont = soup.select_one('.cont')
    infor = ''.join(basic_cont.text.strip().split())
    Name = infor.split('（')[0]
    Year = re.findall('2\d+', infor)[0]
    Piao = re.findall('\d+\.\d?万', infor)[0]
    Type = re.split('类型', infor)[1].split('片长')[0].replace('：', '')
    try:
        Length = re.findall('\d+min', infor)[0]
    except:
        Length = 'null'
        print('该片时长缺失')

    Time = re.findall('\d+\-\d+\-\d+', infor)[0]
    content = [Name, Year, Piao, Type, Length, Time]
    print(j)
    print(content)
    with open('piao.csv', 'a+', newline = '\n')as f:
        w1 = csv.writer(f)
        w1.writerow(content)

       # 获取电影主要人员及幕后公司信息
    pc_infor = soup.select_one('.dltext').text
    infor1 = '\n'.join(pc_infor.strip().split())
    Eng = re.findall('[a-zA-Z\.\,\&\d]+', infor1)
    for e in Eng:
        infor1 = infor1.replace(e, '').replace('（）', '').replace('()', '').replace('\n', ' ')

    index1 = infor1.index('主演')
    index2 = infor1.index('制作')
    index3 = infor1.index('发行')
    Guide = infor1[3:index1]
    Main_Actor = infor1[index1 + 3:index2]
    Made_com = infor1[index2 + 5:index3]
    Form_com = infor1[index3 + 5:]

    # 写入对应的文本文件
    with open('Guide.txt', 'a+') as f1:
        f1.write(Guide)
    with open('Actor.txt', 'a+') as f2:
        f2.write(Main_Actor)
    with open('Company.txt', 'a+')as f3:
        f3.write(Made_com + Form_com)


if __name__ == '__main__':
    j = 0
    print('----------------------------------开始写入中国电影票房前200数据----------------------------')
    with open('piao.csv', 'a+', newline = '\n') as f:
        w = csv.writer(f)
        w.writerow(['导演', '年份', '票房', '类型', '片长', '上映时间'])
    for i in range(1, 21, 1):
        src = 'http://www.cbooo.cn/Mdata/getMdata_movie?area=50&type=0&year=0&initial=%E5%85%A8%E9%83%A8&pIndex=' + str(i)
        getHtml(src)
    print('----------------------------------写入数据完成----------------------------')
