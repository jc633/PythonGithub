# encoding:utf-8
from django.conf.urls import url
from User import views

urlpatterns = [
    url(r'^sign/act=(?P<act>\w+)', views.sign, name='sign'),
    url(r'^account/vertify_regist', views.doRegist, name='doRegist'),
    url(r'^account/vertify_login', views.doLogin, name='doLogin'),
    url(r'logout', views.logout, name='logout'),
    url(r'util/(?P<uId>\d+)/(?P<util>\w+)',
        views.utilDeal, name='utilDeal'),
    url(r'alterInfor', views.alterInfor, name='alterInfor'),
    url(r'^get_vertify/', views.getVertify),
    url(r'^activeAccount$', views.activeUser, name='activeUser'),  # 激活账号页面
    url(r'^emailVertify', views.emailVertify, name='emailVertify'),  # 邮箱验证
    url(r'^send/activeEmail/', views.send_active_Email),  # 发送激活邮件
]
