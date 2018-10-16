# coding:utf-8
'''
@Created on :2018-10-15
@function:定义用户类
@author: jxc
'''
from django.db import models

# 用户类
class user(models.Model):
    uName = models.CharField(max_length=20, null=False)  # 用户名
    uPwd = models.CharField(max_length=40, null=False)  # 密码
    uSex = models.CharField(max_length=4, null=True)  # 性别
    uBornDate = models.CharField(max_length=20, null=True)  # 出生年月
    uPhone = models.CharField(
        primary_key=True, max_length=20, null=False)  # 手机号
    uEmail = models.CharField(max_length=30, null=True)  # 电子邮箱
    uImg = models.ImageField(upload_to='img/user/')  # 用户头像
    uTime = models.CharField(max_length=20, null=True)  # 注册时间

    class Meta:
        db_table = 'user'  # 更改表名

    def __str__(self):
        return models.Model.__str__(self)
