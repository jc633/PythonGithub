# coding:utf-8
'''
@Created on :2018-10-15
@function:自定义字段类型 listfiled
@author: jxc
'''
from django.db import models
import ast

class ListField(models.TextField):
    description = 'self_define ListField'

    def __init__(self):
        return super(ListField, self).__init__()

    # 将数据库数据转为Python格式
    def to_python(self, value):
        if not value:
            value = []
            return value
        if isinstance(value, list):
            return value
        return ast.literal_eval(value)

    def from_db_value(self, value):
        if not value:
            value = []
            return value
        if isinstance(value, list):
            return value
        return ast.literal_eval(value)

    # 将list数据转为str类型
    def get_db_prep_value(self, value, connection, prepared=False):
        if not value:
            return value
        if isinstance(value, list):
            return str(value)

    def value_to_string(self, value):
        if not value:
            return value
        if isinstance(value, list):
            return str(value)
