# coding:utf-8
'''
@Created on :2018-10-16
@function:登录需求中间件
@author: jxc
'''
from django.utils.deprecation import MiddlewareMixin
from GoodComputer import settings
from django.http import HttpResponseRedirect

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        exclude = ['login', 'regist', 'index', 'search', 'logout']
        for ex in exclude:
            if ex in request.path:
                return
        if not request.has_key('uName'):
            return HttpResponseRedirect(settings.LOGIN_URL)
