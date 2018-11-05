# coding:utf-8
'''
@Created on :2018-10-29
@function:用户操作类
@author: jxc
'''
from CommonUtils.stringUtils import stringUtil
from CommonUtils.sqlUtils import sqlUtil
from CommonUtils.imgUtils import imgUtil
from django.contrib import auth
from User.models import user
from User.emailService import emailUtil


stringutil = stringUtil()
sql_user = sqlUtil(user)
emailutil = emailUtil()

# 注册

class userUtil():
    def regist(self, request):
        check = request.POST.get('check')
        if check == request.session['check']:
            del request.session['check']
            code = request.POST.get('vertify')
            if code == request.session['code']:
                uPhone = request.POST.get('phone')
                uEmail = request.POST.get('email')
                if not self.queryUser({'uPhone': uPhone}, order_by='uPhone'):
                    if not self.queryUser({'uEmail': uEmail}):
                        uPwd = request.POST.get('password')
                        u = user()
                        u.uId = stringutil.getRnDigit(6)
                        u.is_Active = False  # 默认未激活
                        u.uName = stringutil.getRnStr(8)
                        u.uPhone = uPhone
                        u.password = stringutil.jiamiString(uPwd)
                        u.uEmail = uEmail
                        u.uSex = None
                        u.email_active = False
                        u.uImg = 'img/user/default_user.png'
                        u.uTime = stringutil.getDate()
                        if sql_user.add(u):
                            return emailutil.send_Email(uEmail, '激活账号')
                        else:
                            return '*注册失败'
                    return '*该邮箱已经被注册了'
                return '*该手机号已经被注册了'
            return '*验证码错误'
        return '*请勿重复提交'

    # 登录
    def login(self, request):
        check = request.POST.get('check')
        if check == request.session['check']:
            account = request.POST.get('account')
            password = request.POST.get('password')
            u = auth.authenticate(account=account, password=password)
            if isinstance(u, user):
                if u.is_Active:
                    auth.login(request, u)
                    return True
                else:
                    return '*抱歉,此账号未被激活或已被禁用'
            return '*账号或密码错误'
        return '*请勿重复提交'

    # 退出登录
    def logout(self, request):
        auth.logout(request)
        return True

    # 修改用户信息
    def alterUser(self, request):
        u = request.user
        if 'userImg' in request.FILES:
            img = request.FILES.get('userImg')
            upImg = imgUtil('/img/user/', img.name)
            u.uImg = upImg.imgDir + upImg.change_upImg_name(u.uId)
            upImg.saveImg(img)
        if 'uName' in request.POST:
            name = request.POST.get('uName')
            if u.uName != name:
                u.uName = name
        if 'sex' in request.POST:
            u.uSex = request.POST.get('sex')
        if 'email' in request.POST:
            u.uEmail = request.POST.get('email')
        if 'oldPwd' in request.POST:
            if stringutil.jiemiString(u.password) == request.POST.get('oldPwd'):
                u.password = stringutil.jiamiString(request.POST.get('newPwd'))
            else:
                return '<script>alert("原密码错误");</script>'
        try:
            u.save()
            return '<script>alert("信息保存成功!");</script>'
        except Exception as e:
            print(e)
            return '<script>alert("信息保存失败");</script>'

    # 查询用户
    def queryUser(self, args, **kwargs):
        if isinstance(args, dict):
            return sql_user.select(args, **kwargs)
        return False

    # 发送邮件
    def send_email(self, email, **kwargs):
        data = self.queryUser({'uEmail': email}, order_by='uEmail')  # 验证用户是否存在
        if data:
            if 'pwd' in kwargs:
                pwd = kwargs['pwd']
                u = data[0]
                if u.password == stringutil.jiamiString(pwd):
                    vertify_type = '激活账号'
                else:
                    return '密码错误'
            else:
                vertify_type = '重置密码'
            return emailutil.send_Email(email, vertify_type)
        else:
            return '账号错误或不存在'
