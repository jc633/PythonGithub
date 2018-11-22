# coding:utf-8
from django.shortcuts import render, redirect, render_to_response
from django.http.response import HttpResponse, JsonResponse
from User.userUtils import userUtil
from django.urls.base import reverse
from CommonUtils.vertifyUtils import vertifyCode
from django.conf import settings
import random
# Create your views here.

userutil = userUtil()


# 404错误
def page_not_found(request):
    return render_to_response('404.html')

# 动态获取头像图片
def get_user_img(request):
    path = settings.MEDIA_ROOT + str(request.user.uImg)
    with open(path, 'rb')as f:
        img_data = f.read()
    return HttpResponse(img_data, content_type='image/jpg')


# 平台首页
def index(request):
    return render(request, 'index.html')


# 登录/注册页面
def sign(request, act='login', msg=None):
    check_html = getToken(request)
    return render(request, 'sign.html', {'act': act, 'msg': msg, 'check': check_html})


# 处理注册信息
def doRegist(request):
    msg = userutil.regist(request)
    if msg == '发送成功' or msg == '发送失败':
        # 转到激活提醒页面
        return redirect(reverse('activeUser', args=(0,)))
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


# 账号设置
def accountSet(request):
    return render(request, 'accountSet.html')

# 个人主页
def myPage(request):
    data = userutil.getMyPage_data(request)
    return render(request, 'myPage.html', {'user': data})

# 意见反馈页面
def feedBack_page(request):
    return render(request, 'feedBack.html')

# 加载意见数据
def load_feedBack(request):
    data = userutil.load_feedBack()
    return HttpResponse(data)

# 发表意见反馈
def suggest(request):
    msg = userutil.save_feedBack(request)
    if msg:
        text = '发表成功,感谢你对易图表的支持!'
    else:
        text = '发表失败,再试一次吧...'
    return HttpResponse(text)

# 修改用户信息
def alterInfor(request):
    msg = userutil.alterUser(request)
    return HttpResponse(msg)

# 账号激活页面
def activeUser_page(request, resend=1):
    return render(request, 'activeAccount.html', {'resend': resend})

# 重置密码页面
def resetPwd_page(request, resetVertify_pass=False):
    if request.session.has_key('resetVertify_pass'):
        resetVertify_pass = request.session['resetVertify_pass']
        del request.session['resetVertify_pass']
    return render(request, 'resetPwd.html', {'resetVertify_pass': resetVertify_pass})

# 修改邮箱页面
def alterEmail_page(request, alterVertify_pass=False):
    if request.session.has_key('alterVertify_pass'):
        alterVertify_pass = request.session['alterVertify_pass']
        del request.session['alterVertify_pass']
    return render(request, 'alterEmail.html', {'alterVertify_pass': alterVertify_pass})

# 重置密码
def resetPassword(request):
    if request.method == 'POST':
        msg = userutil.reset_password(request)
        return HttpResponse(msg)


# 发送账号激活邮件
def send_activeAccount_Email(request):
    if request.is_ajax():
        email = request.POST.get('email')
        msg = userutil.send_email(request, email, '激活账号')
        return HttpResponse(msg)
    pass

# 发送绑定邮箱邮件
def send_bandEmail_Email(request):
    if request.is_ajax():
        email = request.POST.get('email')
        msg = userutil.send_email(request, email, '绑定邮箱')
        return HttpResponse(msg)
    pass

# 发送密码重置邮件
def send_resetPwd_Email(request):
    if request.is_ajax():
        email = request.POST.get('email')
        msg = userutil.send_email(request, email, '重置密码')
        return HttpResponse(msg)
    pass

# 发送修改邮箱邮件
def send_alterEmail_Email(request):
    if request.is_ajax():
        email = request.user.email
        msg = userutil.send_email(request, email, '修改邮箱')
        return HttpResponse(msg)
    pass

# 邮箱验证
def emailVertify(request):
    act = request.GET.get('act')
    if act == 'activeUser':
        msg = userutil.activeAccount(request)
    if act == 'resetPwd':
        msg = userutil.Email_vertify(request)
        if msg == True:
            request.session['resetVertify_pass'] = True
            request.session['reset_email'] = request.GET.get('email')
            return redirect(reverse('resetPwd'))
    if act == 'alterEmail':
        msg = userutil.Email_vertify(request)
        if msg == True:
            request.session['alterVertify_pass'] = True
            return redirect(reverse('alterEmail'))
    if act == 'bandEmail':
        msg = userutil.bandEmail(request)
    return render(request, 'infor.html', {'msg': msg})

# 获取验证码
def getVertifyCode(request):
    # 默认验证码对象
    vertify = vertifyCode(90, 35, (255, 255, 255), 5,
                          'static/font/SIMHEI.TTF', None, None)
    return HttpResponse(vertify.saveInMemory(request))

# 实时验证验证码
def vertifyCode_check(request):
    code = request.GET.get('code')
    if code == request.session['code']:
        return HttpResponse('*输入正确')
    return HttpResponse('*输入错误')

# 生成检验令牌，防止用户多次提交
def getToken(request):
    check = str(random.randint(1000, 20000))
    request.session['check'] = check
    html = '<input type="hidden" name="check" value=' + check + '>'
    return html
