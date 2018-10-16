# coding:utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http import HttpResponse
from CommonUtils.vertifyUtils import vertifyCode
from CommonUtils.stringUtils import stringUtil
from io import BytesIO
from User.userUtils import Admin
from django.http.response import HttpResponseRedirect

# 实例化操作类
admin = Admin()
stringutil = stringUtil()

# 系统首页
def index(request):
    return render(request, 'index.html')

# 注册页面
def regist(request, mes=''):
    return render(request, 'Regist.html', {'failMessage': mes})

# 处理注册信息
def doRegist(request):
    mes = admin.addUser(request)
    if mes == True:
        return HttpResponseRedirect('/user/login')
    return regist(request, mes)

# 登录页面
def login(request, mes=''):
    return render(request, 'Login.html', {'failMessage': mes})

# 处理登录信息
def doLogin(request):
    uPhone = request.POST.get('usercount')
    u = admin.selectUser({'uPhone': uPhone})
    if not u:
        return login(request, '*账号错误或不存在')
    if stringutil.jiemiString(u.uPwd) == request.POST.get('password'):
        request.session['uName'] = u.uName
        return HttpResponseRedirect('/user/index')
    return login(request, '*密码错误')


# 退出登录
def logout(request):
    try:
        del request.session['uName']
        return HttpResponseRedirect('/user/login')
    except Exception as e:
        print(e)

# 查看购物车
def shoppingCar(request):
    return HttpResponse('正在建设中')

# 查看我的收藏
def myCollect(request):
    return HttpResponse('正在建设中')

# 进入购物车
def userCenter(request):
    return HttpResponse('正在建设中')

# 进入购物车
def shopCenter(request):
    return HttpResponse('正在建设中')

# 生成验证码图片
def vertifyImg(request):
    # 默认验证码对象
    vertify = vertifyCode(80, 34, (255, 255, 255), 5,
                          'static/font/SIMHEI.TTF', None, None)
    img = vertify.getVertifyImg(request)
    f = BytesIO()
    img.save(f, 'png')
    return HttpResponse(f.getvalue())
