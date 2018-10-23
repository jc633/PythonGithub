# coding:utf-8
from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http import HttpResponse
from CommonUtils.vertifyUtils import vertifyCode
from CommonUtils.stringUtils import stringUtil
from io import BytesIO
from User.userUtils import userUtil
from Product.shopUtils import shopManage
from django.http.response import HttpResponseRedirect

# 实例化操作类
userutil = userUtil()
stringutil = stringUtil()
shopmanage = shopManage()

# 系统首页
def index(request):
    return render(request, 'index.html')

# 用户注册页面
def regist(request, mes=''):
    return render(request, 'Regist.html', {'failMessage': mes})

# 处理用户注册信息
def doRegist(request):
    mes = userutil.addUser(request)
    if mes == True:
        return HttpResponseRedirect('/user/login')
    return regist(request, mes)

# 用户登录页面
def login(request, mes=''):
    return render(request, 'Login.html', {'failMessage': mes})

# 处理用户登录信息
def doLogin(request):
    uPhone = request.POST.get('usercount')
    u = userutil.selectUser({'uPhone': uPhone})
    if not u:
        return login(request, '*账号错误或不存在')
    if stringutil.jiemiString(u[0].uPwd) == request.POST.get('password'):
        request.session['uName'] = u[0].uName
#         request.session.set_expiry(60 * 10)  # 设置失效时间为10分钟
        return HttpResponseRedirect('/user/index')
    return login(request, '*密码错误')


# 退出登录
def logout(request):
    try:
        del request.session['uName']
        return HttpResponseRedirect('/user/login')
    except Exception as e:
        print(e)

# 免费开店
def openShop(request):
    msg = shopmanage.addShop(request)
    return render(request, 'Message.html', {'msg': msg})


# 查看购物车
def shoppingCar(request):
    return HttpResponse('正在建设中')

# 查看我的收藏
def myCollect(request):
    return HttpResponse('正在建设中')

# 进入用户中心
def userCenter(request):
    return HttpResponse('正在建设中')

# 进入卖家中心
def shopCenter(request):
    util = request.GET.get('util')
    if util:
        if util == 'freeOpenShop':
            html = 'business/freeOpenShop.html'
        if util == 'releaseProduct':
            if shopmanage.isOpenShop(request):
                html = 'business/releaseProduct.html'
            else:
                return Message(request, '你还没有开店,无法发布商品!')
        return render(request, 'business/businessCenter.html', {'html_name': html})
    return render(request, 'business/businessCenter.html')

# 信息提示页面
def Message(request, msg):
    return render(request, 'Message.html', {'msg': msg})

# 生成验证码图片
def vertifyImg(request):
    # 默认验证码对象
    vertify = vertifyCode(80, 34, (255, 255, 255), 5,
                          'static/font/SIMHEI.TTF', None, None)
    return HttpResponse(vertify.saveInMemory(request))
