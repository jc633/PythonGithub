# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http.response import HttpResponse

# Create your views here.


#

# 查看库存列表
def listProduct(request):
    return HttpResponse('正在建设中')
