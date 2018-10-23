# coding:utf-8
# 添加品牌分类数据
from django.test import TestCase

# Create your tests here.
import django
django.setup()
from CommonUtils.stringUtils import stringUtil
from Product.models import category
import os
from django.db import connection
# os.chdir('C:\\Users\\Administrator\\Desktop')
#
# if __name__ == '__main__':
#     stringutil = stringUtil()
#     cursor = connection.cursor()
#     cat = []
#     with open('cat.txt', 'r')as f:
#         for t in f.readlines():
#             catId = 'cat_' + stringutil.getRnDigit(5)
#             catName = t.strip().split(' ')[1].replace(
#                 '（', '(').replace('）', ')')
#
#             cat.append({catId: catName})
#             sql = "insert into category values('%s','%s','None')" % (
#                 catId, catName)
#             cursor.execute(sql)
#             connection.commit()
#         print(cat)
