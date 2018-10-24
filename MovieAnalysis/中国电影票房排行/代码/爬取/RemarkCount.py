# coding:utf-8
''' 
  function:自动获取并写入票房排行前50的电影评价人数
'''
import sys
import os
from  selenium import webdriver
from bs4 import BeautifulSoup as bs
import xlrd
import csv
os.chdir(r'C:\Users\Administrator\Desktop')
sys.setrecursionlimit(9000)


# 自动获取电影的评论数
# para:电影名
def getRemark(movie_name):
    option = webdriver.ChromeOptions()
    option.add_argument('head')
    dr = webdriver.Chrome(chrome_options = option)
    dr.get('https://movie.douban.com/')
    dr.find_element_by_id('inp-query').send_keys(movie_name)
    dr.find_element_by_class_name('inp-btn').click()
    try:
        dr.find_element_by_partial_link_text(movie_name).click()
        soup = bs(dr.page_source, 'lxml')
        dr.quit()
        return soup.select_one('.rating_sum').text
    except:
        return 'null'


def write(name):
    count = getRemark(name)
    print(name, count)
    with open('remark.csv', 'a+', newline = '\n')as f:
        w = csv.writer(f)
        w.writerow([name, count])


if __name__ == '__main__':
    print('----------------------开始获取并写入票房排行前50的电影评价人数-------------------------')
    wb = xlrd.open_workbook('piao.xlsx', 'r')
    ws = wb.sheets()[0]
    names = ws.col_values(0)
    for i in range(1, 51):
        write(names[i])
    print('--------------------写入数据完成-----------------------------------------')
