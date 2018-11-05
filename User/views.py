# coding:utf-8
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from User.userUtils import userUtil
from django.urls.base import reverse
from CommonUtils.vertifyUtils import vertifyCode
import random
# Create your views here.

userutil = userUtil()
# 平台首页

def index(request):
    return render(request, 'index.html')

# 登录/注册页面
def sign(request, act='login', msg=None):
    check_html = getToken(request)
    return render(request, 'sign.html', {'act': act, 'msg': msg, 'check': check_html})

# 账号激活
def activeUser(request):
    return render(request, 'activeAccount.html')

# 处理注册信息
def doRegist(request):
    msg = userutil.regist(request)
    if msg == '发送成功' or msg == '发送失败':
        # 转到激活提醒页面
        return redirect(reverse('activeUser'))
    return sign(request, 'regist', msg)

# 处理登录信息
def doLogin(request):
    msg = userutil.login(request)
    if msg == True:
        #         request.session.set_expiry(60 * 5)  # 设置session有效期为5分钟
        return redirect(reverse('index'))
    return sign(request, 'login', msg)

# 退出登录
def logout(request):
    try:
        if userutil.logout(request):
            return redirect(reverse('index'))
    except Exception as e:
        print(e)


# 用户操作处理
def utilDeal(request, uId, util):
    return render(request, 'userUtil.html')

# 修改用户信息
def alterInfor(request):
    msg = userutil.alterUser(request)
    return HttpResponse(msg)


# 发送激活邮件
def send_active_Email(request):
    if request.is_ajax():
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        msg = userutil.send_email(email, pwd=pwd)
        return HttpResponse(msg)
    pass

# 邮箱验证
def emailVertify(request):
    return HttpResponse('恭喜你，账号已成功激活!')

# 获取验证码
def getVertify(request):
    # 默认验证码对象
    vertify = vertifyCode(90, 35, (255, 255, 255), 5,
                          'static/font/SIMHEI.TTF', None, None)
    return HttpResponse(vertify.saveInMemory(request))

# 生成检验令牌，防止用户多次提交
def getToken(request):
    check = str(random.randint(1000, 20000))
    request.session['check'] = check
    html = '<input type="hidden" name="check" value=' + check + '>'
    return html
