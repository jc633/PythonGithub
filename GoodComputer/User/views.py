# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse

# Create your views here.

# 系统首页
def index(request):
    return HttpResponse('我是一个人')

# 注册页面
def regist(request):
    return render(request, 'Regist.html')

# 登录页面
def login(request):
    return render(request, 'Login.html')
