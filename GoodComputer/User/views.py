# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse

# Create your views here.

# 系统首页
def index(request):
    return HttpResponse('我是一个人')
