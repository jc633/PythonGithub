# coding:utf-8
'''
@Created on :2018-10-16
@function:登录需求中间件
@author: jxc
'''
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        exclude = ['login', 'regist', 'index',
                   'search', 'logout', 'doLogin', 'doRegist', 'get-vertify']
        for ex in exclude:
            if ex in request.path:
                return
        if not request.session.has_key('uName'):
            return render(request, 'Message.html', {'msg': '请先登录!'})
