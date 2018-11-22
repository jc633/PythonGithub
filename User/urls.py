# encoding:utf-8
from django.conf.urls import url
from User import views

hander404 = views.page_not_found
urlpatterns = [
    url(r'^sign/act=(?P<act>\w+)', views.sign, name='sign'),
    url(r'^get_user_img/.*$', views.get_user_img, name='getUserImg'),  # 获取用户头像
    url(r'^feedBack$', views.feedBack_page, name='feedBack'),  # 意见反馈页面
    url(r'^loading/feedBack', views.load_feedBack,
        name='loadFeedBack'),  # 意见反馈数据加载
    url(r'suggest/', views.suggest, name='suggest'),  # 发表意见反馈
    url(r'^account/vertify_regist', views.doRegist, name='doRegist'),
    url(r'^account/vertify_login', views.doLogin, name='doLogin'),
    url(r'logout', views.logout, name='logout'),
    url(r'util/accountSet', views.accountSet, name='accountSet'),
    url(r'util/myPage', views.myPage, name='myPage'),
    url(r'alterInfor', views.alterInfor, name='alterInfor'),  # 修改用户信息
    url(r'^get_vertify/', views.getVertifyCode),  # 获取图片验证码
    url(r'^vertifyCode/check', views.vertifyCode_check),  # 验证码实时验证
    url(r'^activeAccount/resend=(?P<resend>[0|1])/',
        views.activeUser_page, name='activeUser'),  # 转到激活账号页面
    url(r'resetPwd/', views.resetPwd_page, name='resetPwd'),  # 转到重置密码页面
    url(r'alterEmail/', views.alterEmail_page, name='alterEmail'),  # 转到修改邮箱页面
    url(r'^send/email/activeAccount/', views.send_activeAccount_Email),  # 发送激活账户邮件
    url(r'^send/email/bandEmail', views.send_bandEmail_Email),  # 发送激活邮箱邮件
    url(r'send/email/resetPwd', views.send_resetPwd_Email),  # 发送重置密码邮件
    url(r'send/email/alterEmail', views.send_alterEmail_Email),  # 发送修改邮箱邮件
    url(r'^emailVertify', views.emailVertify, name='emailVertify'),  # 邮箱验证
    url(r'^handle/resetPassword', views.resetPassword),  # 重置密码操作
]
