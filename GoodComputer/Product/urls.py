# coding:utf-8
'''
@Created on :2018-10-14
@function:Product的路由
@author: jxc
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list-product', views.listProduct, name='listProduct'),
    url(r'^releaseProduct', views.releaseProduct, name='releaseProduct'),
    url(r'action\/act=(?P<act>\S+)\&id=(?P<proId>\S+)',
        views.productAct, name='actDeal'),

]
