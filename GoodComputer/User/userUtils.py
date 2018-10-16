# coding:utf-8
'''
@Created on :2018-10-15
@function:定义管理员类
@author: jxc
'''
from User.models import user
from CommonUtils.stringUtils import stringUtil
# 实例化操作类
stringutil = stringUtil()

class Admin():
    def addUser(self, request):
        code = request.POST.get('code').lower()
        if code == request.session['code']:
            uName = request.POST.get('username')
            uPhone = request.POST.get('phone_number')
            uPwd = request.POST.get('password')
            uTime = stringutil.getDate()
            u = user(uName, uPwd, None, None, uPhone, None, None, uTime)
            try:
                u.save()
                return True
            except Exception as e:
                print(e)
                return False
        return '验证码错误'
