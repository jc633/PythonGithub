# coding:utf-8
from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse
from CommonUtils.vertifyUtils import vertifyCode
from io import BytesIO
from User.userUtils import Admin
from django.http.response import HttpResponseRedirect

# 实例化操作类
admin = Admin()

# 系统首页
def index(request):
    return HttpResponse('我是一个人')

# 登录页面
def login(request):
    return render(request, 'Login.html')

# 处理登录信息
def doLogin(request):
    return HttpResponseRedirect('/user/index')

# 注册页面
def regist(request):
    return render(request, 'Regist.html')

# 处理注册信息
def doRegist(request):
    mes = admin.addUser(request)
    if mes == True:
        return render(request, 'Login.html')
    return render(request, 'Regist.html', {'failMessage': mes})


# 生成验证码图片
def vertifyImg(request):
    # 默认验证码对象
    vertify = vertifyCode(80, 34, (255, 255, 255), 5,
                          'static/font/SIMHEI.TTF', None, None)
    img = vertify.getVertifyImg(request)
    f = BytesIO()
    img.save(f, 'png')
    return HttpResponse(f.getvalue())
