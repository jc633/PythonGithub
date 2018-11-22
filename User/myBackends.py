# coding:utf-8
'''
@Created on :2018-10-29
@function: 自定义登录验证后台
@author: jxc
'''
from User.models import user
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class CustomLoginBackend(ModelBackend):
    def authenticate(self, account=None, password=None):
        try:
            u = user.objects.get(uEmail=account)
        except user.DoesNotExist:
            return None
        else:
            if u.check_password(password):
                return u
            else:
                return None
        return None

    def get_user(self, user_id):
        try:
            return user.objects.get(uId=user_id)
        except user.DoesNotExist:
            return None
