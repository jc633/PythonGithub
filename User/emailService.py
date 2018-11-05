# coding:utf-8
'''
@Created on :2018-11-05
@function:定义有关邮件操作类
@author: jxc
'''
from celery_tasks.tasks import Mailer
from CommonUtils.sqlUtils import sqlUtil
from CommonUtils.stringUtils import stringUtil
from User.models import email_vertify


sql_email = sqlUtil(email_vertify)
mailer = Mailer()  # 邮件对象
stringutil = stringUtil()

class emailUtil():
    def __init__(self):
        self.email = ''
        self.vertify_type = ''

    # 发送邮件(包括激活账号和重置密码)
    def send_Email(self, email, vertify_type):
        self.email = email
        self.vertify_type = vertify_type
        if not self.sended_check():
            eVertify = self.add_email_vertify()
            mailer.subtype = 'html'
            mailer.debug = True
            code = stringutil.get_md5_string(eVertify.code)
            time = eVertify.send_time
            if vertify_type == '激活账号':
                subject = '易图表平台账号激活'
                act = 'activeUser'
                con1 = '感谢你使用易图表'
                con2 = '请点击右侧的激活链接激活账号:'
            else:
                subject = '易图表平台密码重置'
                act = 'resetPwd'
                con1 = ''
                con2 = '请点击右侧的链接重置密码:'
            mailer.subject = subject
            url = '<a href=http://10.6.31.21:8000/user/emailVertify?act=' + act + '&email=' + \
                email + '&s=' + code + '&t=' + time + '> ' + 'http://10.6.31.21/user/emailVertify?act=' + act + '&email=' + \
                email + '&s=' + code + '&t=' + time + '</a>'
            mailer.content = '<p style="font-size:20px;">' + con1 + \
                '</p><p style="font-size:18px">' + con2 + url + '</p>'
            if mailer.send_mail(email):  # 如果发送成功
                if sql_email.add(eVertify):  # 将发送记录添加到数据库
                    return '发送成功'
            return '发送失败'
        return '有邮件未失效,无法重发'

    # 发送检测，检测是否已发过仍在有效期内的邮件
    def sended_check(self):
        data = sql_email.select(
            {'email': self.email, 'vertify_type': self.vertify_type, 'is_live': 1}, connect_type='and', order_by='email')
        if data:
            return True
        return False

    # 添加邮件发送记录,返回邮件验证对象
    def add_email_vertify(self):
        eVertify = email_vertify()
        eVertify.email = self.email
        eVertify.code = stringutil.getRnStr(10)
        eVertify.send_time = stringutil.getTimeStamp()
        eVertify.is_live = True
        eVertify.vertify_type = self.vertify_type
        return eVertify
