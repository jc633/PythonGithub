# coding:utf-8
'''
@Created on :2018-11-05
@function:定义有关邮件操作类
@author: jxc
'''
from celery_tasks.tasks import Mailer
from CommonUtils.sqlUtils import sqlUtil
from CommonUtils.stringUtils import stringUtil
from Inform.models import email_vertify
from datetime import datetime
import time


sql_email = sqlUtil(email_vertify)
mailer = Mailer()  # 邮件对象
stringutil = stringUtil()

class emailUtil():
    def __init__(self):
        self.email = ''
        self.vertify_type = ''

    # 发送邮件(包括激活账号、重置密码、修改邮箱、邮箱绑定)
    def send_Email(self, email, vertify_type):
        self.email = email
        self.vertify_type = vertify_type
        if vertify_type == '激活账号':
            overTime = self.send_check('day', 3)
            subject = '易图表-用户账号激活'
            act = 'activeUser'
            con1 = '感谢你使用易图表'
            con2 = '请点击右侧的激活链接激活账号:'
        if vertify_type == '重置密码':
            overTime = self.send_check('minute', 10)
            subject = '易图表-用户密码重置'
            act = 'resetPwd'
            con1 = ''
            con2 = '请点击右侧的链接重置密码:'
        if vertify_type == '修改邮箱':
            overTime = self.send_check('minute', 10)
            subject = '易图表-用户邮箱更改'
            act = 'alterEmail'
            con1 = '频繁修改邮箱有被盗号风险，请谨慎操作!'
            con2 = '请点击右侧的链接进行身份验证:'
        if vertify_type == '绑定邮箱':
            overTime = self.send_check('minute', 10)
            subject = '易图表-用户邮箱绑定'
            act = 'bandEmail'
            con1 = '绑定邮箱,操作更安全'
            con2 = '请点击右侧的链接进行邮箱绑定:'
        if overTime:
            eVertify = self.add_vertify_record()
            mailer.subtype = 'html'
            mailer.debug = True
            code = stringutil.get_md5_string(eVertify.code)
            time = str(eVertify.send_time)
            mailer.subject = subject
            url = '<a href=http://10.6.31.21:8000/user/emailVertify?act=' + act + '&email=' + \
                email + '&s=' + code + '&t=' + time + '> ' + 'http://10.6.31.21/user/emailVertify?act=' + act + '&email=' + \
                email + '&s=' + code + '&t=' + time + '</a>'
            mailer.content = '<p style="font-size:20px;">' + '<strong>' + con1 + '</strong>' + \
                '</p><p style="font-size:18px">' + con2 + url + \
                '</p><p style="font-size:18px">若非本人操作,请忽略该邮件</p>'
            if mailer.send_mail(email):  # 如果发送成功
                if sql_email.add(eVertify):  # 将发送记录添加到数据库
                    return '发送成功'
            return '发送失败'
        return '有邮件未失效,无法重发'

    # 邮件过期检测
    def overTime_check(self, oldTime, newTime, timeKind, validTime):
        try:
            if oldTime > newTime:
                oldTime, newTime = newTime, oldTime
            d1 = datetime.utcfromtimestamp(oldTime)
            d2 = datetime.utcfromtimestamp(newTime)
            if timeKind == 'day':
                if (d2 - d1).days > validTime:
                    return True
                return False
            if timeKind == 'minute':
                if (d2 - d1).seconds > validTime * 60:
                    return True  # 过期
                return False
        except Exception as e:
            print(e)

    # 发送检测，检测是否发过检测或之前发的邮件是否已过期，若已过有效期,将is_live改为false
    def send_check(self, timeKind, validTime):
        newTime = stringutil.getTimeStamp()
        data = self.queryEmail(
            {'email': self.email, 'vertify_type': self.vertify_type, 'is_live': 1}, connect_type='and', order_by='email')
        if data:
            e = data[0]
            oldTime = e.send_time
            if self.overTime_check(oldTime, newTime, timeKind, validTime):  # 如果之前发的邮件过期
                e.is_live = False
                sql_email.add(e)
                return True
            return False
        return True  # 未发过邮件

    # 添加邮件发送记录,返回邮件验证对象
    def add_vertify_record(self):
        eVertify = email_vertify()
        eVertify.email = self.email
        eVertify.code = stringutil.getRnStr(10)
        eVertify.send_time = stringutil.getTimeStamp()
        eVertify.is_live = True
        eVertify.vertify_type = self.vertify_type
        return eVertify

    # 邮件有效检测(验证码是否正确、是否失效)
    def email_valid_check(self, vertify_type, email, code, oldTime):
        try:
            oldTime = int(oldTime)
        except:
            return '链接错误'
        newTime = stringutil.getTimeStamp()
        data = self.queryEmail(
            {'email': email, 'vertify_type': vertify_type, 'is_live': 1}, order_by='email')
        if data:
            e = data[0]
            # 激活邮件3天后失效
            if vertify_type == '激活账号' and self.overTime_check(oldTime, newTime, 'day', 3):
                return '该链接已失效!请<a href="/user/activeAccount/resend=1">重新获取激活链接</a>'
            # 重置密码邮件10分钟后失效
            if vertify_type == '重置密码' and self.overTime_check(oldTime, newTime, 'minute', 10):
                return '该链接已失效!请<a href="/user/resetPwd">重新获取验证链接</a>'
            if vertify_type == '修改邮箱' and self.overTime_check(oldTime, newTime, 'minute', 10):
                return '该链接已失效!请重新获取验证链接'
            if vertify_type == '绑定邮箱' and self.overTime_check(oldTime, newTime, 'minute', 10):
                return '该链接已失效!请重新获取验证链接'
            if code == stringutil.get_md5_string(e.code):
                e.is_live = False  # 验证成功后将邮件改为无效
                sql_email.add(e)
                return True  # 验证成功
            return '链接错误'
        return '链接错误'

    # 邮件发送记录查询
    def queryEmail(self, args, **kwargs):
        if isinstance(args, dict):
            return sql_email.select(args, **kwargs)
        return False
