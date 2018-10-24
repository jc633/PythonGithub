# coding:utf-8
'''
@Created on :2018-10-15
@function:定义管理员类
@author: jxc
'''
from User.models import user
from CommonUtils.stringUtils import stringUtil
from CommonUtils.sqlUtils import sqlUtil
from django.db.models import Q
# 实例化操作类
stringutil = stringUtil()
sqlutil = sqlUtil(user)

class userUtil():

    # 注册
    def addUser(self, request):
        code = request.POST.get('code').lower()
        if code == request.session['code']:
            uPhone = request.POST.get('phone_number')
            if self.selectUser({'uPhone': uPhone}):
                return '*该手机号已经被注册了'
            uName = request.POST.get('username')
            if self.selectUser({'uName': uName}):
                return '*该用户名已经被注册了'
            uPwd = request.POST.get('password')
            uTime = stringutil.getDate()
            u = user(uName, stringutil.jiamiString(uPwd),
                     None, None, uPhone, None, None, uTime)
            u.save()
            if sqlutil.add(u):
                return True
            return '*注册失败'
        return '*验证码错误'

    # 查询用户,无参时返回None
    def selectUser(self, args):
        return sqlutil.select(args, 'OR', 'uName')
