# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse
from CommonUtils.vertifyUtils import vertifyCode
from io import BytesIO


# Create your views here.
# 系统首页

def index(request):
    return HttpResponse('我是一个人')

# 注册页面
def regist(request):
    return render(request, 'Regist.html')

# 生成验证码图片
def vertifyImg(request):
    # 默认验证码对象
    vertify = vertifyCode(80, 34, (255, 255, 255), 5,
                          'static/font/SIMHEI.TTF', None, None)
    img = vertify.getVertifyImg(request)
    f = BytesIO()
    img.save(f, 'png')
    return HttpResponse(f.getvalue())

# 登录页面
def login(request):
    return render(request, 'Login.html')
