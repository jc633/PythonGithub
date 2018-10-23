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
    url(r'^doRegist', views.doRegist, name='doRegist'),
    url(r'^login', views.login, name='login'),
    url(r'^doLogin', views.doLogin, name='doLogin'),
    url(r'logout', views.logout, name='logout'),
    url(r'^get-vertify', views.vertifyImg),
    url(r'^look/shoppingCar', views.shoppingCar, name='shoppingCar'),
    url(r'^look/myCollect', views.myCollect, name='myCollect'),
    url(r'^enter/userCenter', views.userCenter, name='userCenter'),
    url(r'^enter/businessCenter', views.shopCenter, name='shopCenter'),
    url(r'^addShop', views.openShop, name='addShop'),

]
