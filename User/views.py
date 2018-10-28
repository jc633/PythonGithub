# coding:utf-8
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# 平台首页
def index(request):
    return render(request, 'index.html')
