# coding:utf-8
'''
@Created on :2018-10-29
@function: 自定义登录验证后台
@author: jxc
'''
from User.models import user
from django.contrib.auth.backends import ModelBackend
from CommonUtils.stringUtils import stringUtil
from django.db.models import Q
stringutil = stringUtil()

class CustomLoginBackend(ModelBackend):
    def authenticate(self, account=None, password=None):
        try:
            u = user.objects.get(Q(uPhone=account) | Q(uEmail=account))
        except user.DoesNotExist:
            return None
        else:
            if password == stringutil.jiemiString(u.password):
                return u
            else:
                return None
        return None

    def get_user(self, user_id):
        try:
            return user.objects.get(uId=user_id)
        except user.DoesNotExist:
            return None
