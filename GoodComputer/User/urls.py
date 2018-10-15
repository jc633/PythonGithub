# coding:utf-8
'''
@Created on :2018-10-14
@function:User的路由
@author: jxc
'''
from django.conf.urls import url
from User import views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^regist', views.regist, name='regist'),
    url(r'^login', views.regist, name='login'),
    url(r'^get-vertify', views.vertifyImg),
]
