# coding:utf-8
'''
@Created on :2018-10-23
@function:product的全文检索
@author: jxc
'''
from haystack import indexes
from Product.models import product

# 类名必须为需要检索的Model_name+Index，这里需要检索product，所以创建productIndex
class productIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return product

    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
