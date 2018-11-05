# coding:utf-8
'''
@Created on :2018-11-03
@function:定义与邮件相关的操作类
@author: jxc
'''
# 在django.core.mail模块提供了send_mail来发送邮件。
#
# send_mail(subject,message,from_email,recipient_list,html_message=None)
#
# subject 邮件标题
# message 普通邮件正文， 普通字符串
# from_email 发件人
# recipient_list 收件人列表
# html_message 多媒体邮件正文，可以是html字符串

from django.core.mail import send_mail
from django.conf import settings


class emailUtil:
    def __init__(self, email_list):
        self.email_list = email_list

    def send_verify_mail(self, url):
        # subject, message, from_email, recipient_list,html_message=None
        subject = '易图表平台激活邮件'
        message = ''
        from_email = settings.EMAIL_FROM  # 发件人
        recipient_list = self.email_list  # 收件人列表
        # 可以传递 html代码
        # 我们需要生成一个url,这个url中的token需要包含用户的id信息(id需要被处理)
        html_message = '<p>尊敬的用户您好！</p>' \
                       '<p>感谢您使用XXXX。</p>' \
                       '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                       '<p><a href="%s">%s<a></p>' % (
                           self.email_list, url, url)
        send_mail(subject, message, from_email,
                  recipient_list, html_message=html_message)
