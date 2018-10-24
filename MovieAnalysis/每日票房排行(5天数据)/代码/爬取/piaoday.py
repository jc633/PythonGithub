# coding:utf-8
'''
  function：获取中国电影网的每日票房前10信息
'''
import requests
import os
import re
from bs4 import BeautifulSoup as bs
from openpyxl import workbook
import csv
import time
os.chdir(r'C:\Users\Administrator\Desktop')
def getHtml(src):
    html = requests.get(src).content.decode('utf-8')
    getInfor(html)

def getInfor(html):
    soup = bs(html, 'lxml')
    infor = soup.select('.trtop')
    time1 = time.strftime('%Y-%m-%d', time.localtime())
    print(time1)
    for i in range(1, 11):
        tds = infor[i].contents  # 得到子节点列表
        name = tds[3].string  # 电影名
        sspf = tds[5].string  # 实时票房
        pfzb = tds[7].string  # 票房占比
        pflj = tds[9].string  # 票房累计
        ppzb = tds[11].string  # 排片占比
        syts = tds[13].string  # 上映天数
        con = [name, sspf, pfzb, pflj, ppzb, syts, time1]
        print(con)
        with open('day.csv', 'a+', newline = '\n')as f:
            w = csv.writer(f)
            w.writerow(con)


if __name__ == '__main__':
    print('---------------------------------开始写入每日票房排行信息---------------------------------')
    src = 'http://www.cbooo.cn/'
    getHtml(src)
    print('---------------------------------写入数据完成---------------------------------')
