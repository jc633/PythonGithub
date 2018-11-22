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
from Inform.emailUtils import emailUtil
from Inform.messageUtils import messageUtil
import json
from django.conf import settings

stringutil = stringUtil()
sql_user = sqlUtil(user)
emailutil = emailUtil()
msgutil = messageUtil()

# 注册

class userUtil():
    def regist(self, request):
        check = request.POST.get('check')
        if check == request.session['check']:
            del request.session['check']
            code = request.POST.get('vertify')
            if code == request.session['code']:
                del request.session['code']
                email = request.POST.get('email')
                # 检测用户是否存在:
                if not self.queryUser({'email': email}, order_by='email'):
                    uPwd = request.POST.get('password')
                    u = user()
                    u.id = stringutil.getRnDigit(6)
                    u.is_active = False  # 默认未激活
                    u.uName = stringutil.getRnStr(8)
#                     u.password = stringutil.jiamiString(uPwd)
                    u.set_password(uPwd)
                    u.email = email
                    u.uSex = None
                    u.email_active = False
                    u.uImg = 'img/user/default_user.png'
                    u.uTime = stringutil.getTimeStamp()
                    if sql_user.add(u):
                        return emailutil.send_Email(email, '激活账号')
                    else:
                        return '*注册失败'
                return '*该邮箱已经被注册了'
            return '*验证码错误'
        return '*请勿重复提交'

    # 登录
    def login(self, request):
        check = request.POST.get('check')
        if check == request.session['check']:
            account = request.POST.get('account')
            password = request.POST.get('password')
            u = auth.authenticate(email=account, password=password)
            if isinstance(u, user):
                if u.is_active:
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
            upImg = imgUtil('img/user/', img.name)
            u.uImg = upImg.imgDir + upImg.change_upImg_name(u.id)
            upImg.saveImg(img)
        if 'uName' in request.POST:
            name = request.POST.get('uName')
            if u.uName != name:
                u.uName = name
        if 'sex' in request.POST:
            u.uSex = request.POST.get('sex')
        if 'email' in request.POST:
            u.email = request.POST.get('email')
        if 'oldPwd' in request.POST:
            if stringutil.jiemiString(u.password) == request.POST.get('oldPwd'):
                u.password = stringutil.jiamiString(request.POST.get('newPwd'))
            else:
                return '<script>alert("原密码错误");</script>'
        try:
            u.save()
            return '<script>alert("信息保存成功!");window.location.href="/user/util/accountSet";</script>'
        except Exception as e:
            print(e)
            return '<script>alert("信息保存失败");</script>'

    # 查询用户
    def queryUser(self, args, **kwargs):
        if isinstance(args, dict):
            return sql_user.select(args, **kwargs)
        return False

    # 激活账号
    def activeAccount(self, request):
        msg = self.Email_vertify(request)
        email = request.GET.get('email')
        if msg == True:
            data = self.queryUser({'email': email}, order_by='id')
            u = data[0]
            if not u.is_active:
                u.is_active = True
                u.email_active = True
                if sql_user.add(u):
                    return '恭喜你!账号已成功激活,3秒后自动跳转到登录页面'
            return '你的账号已激活！可直接登录'
        return msg

    # 重置密码
    def reset_password(self, request):
        if request.session.has_key('reset_email'):
            email = request.session['reset_email']
            del request.session['reset_email']
            email_data = emailutil.queryEmail(
                {'email': email, 'vertify_type': '重置密码'}, connect_type='and', order_by='email')  # 如果有邮件发送记录
            if email_data:
                pwd = request.POST.get('newPwd')
                user_data = self.queryUser({'email': email}, order_by='id')
                if user_data:
                    u = user_data[0]
                    u.password = stringutil.jiamiString(pwd)
                    if sql_user.add(u):
                        return '重置密码成功!'
                    return '重置密码失败'
                return '重置密码失败'
            return '重置密码失败'
        return '请重新进行身份验证'

    # 发送邮件
    def send_email(self, request, email, vertify_type):
        data = self.queryUser({'email': email}, order_by='email')  # 验证用户是否存在
        if data:
            if vertify_type == '激活账号':
                pwd = request.POST.get('password')
                u = data[0]
                if u.is_Active:
                    return '该账号已激活！'
                if u.password == stringutil.jiamiString(pwd):
                    pass
                else:
                    return '密码错误'
            elif vertify_type == '绑定邮箱':
                return '该账号已经存在!'
            else:
                pass
            return emailutil.send_Email(email, vertify_type)
        else:
            if vertify_type == '绑定邮箱':
                return emailutil.send_Email(email, vertify_type)
            return '账号错误或不存在'

    # 绑定邮箱
    def bandEmail(self, request):
        msg = self.Email_vertify(request)
        email = request.GET.get('email')
        if msg == True:
            u = request.user
            u.email = email
            u.email_active = True
            if sql_user.add(u):
                return '邮箱修改成功,3秒后自动跳转到用户设置页面'
            else:
                return '修改失败'
        return msg

    # 邮件验证
    def Email_vertify(self, request):
        act = request.GET.get('act')
        email = request.GET.get('email')
        code = request.GET.get('s')
        oldTime = request.GET.get('t')
        if act == 'activeUser':
            vertify_type = '激活账号'
        if act == 'resetPwd':
            vertify_type = '重置密码'
        if act == 'alterEmail':
            vertify_type = '修改邮箱'
        if act == 'bandEmail':
            vertify_type = '绑定邮箱'
        result = emailutil.email_valid_check(
            vertify_type, email, code, oldTime)
        return result

    # 获取个人主页数据
    def getMyPage_data(self, request):
        user = {}
        user['uImg'] = request.user.uImg
        user['uName'] = request.user.uName
        user['id'] = request.user.id
        user['uSex'] = request.user.uSex
        user['uTime'] = stringutil.strTimeStamp(request.user.uTime, '-')
        return user

    # 保存意见反馈
    def save_feedBack(self, request):
        msg = {}
        msg['content'] = request.GET.get('content')
        msg['type'] = request.GET.get('type')
        replyed_mId = request.GET.get('replyed_mId')
        msgutil.replyed_mId = None if replyed_mId == 'null' else replyed_mId
        msgutil.sendId = request.user.id
        recId = request.GET.get('recId')
        msgutil.recieveId = None if recId == 'null' else recId
        if msgutil.send_msg(msg):
            return True
        return False

    # 生成评论字典数据
    def generateComment_Data(self, subobj):
        value = {}
        value['mId'] = subobj.messageId
        value['rId'] = subobj.recieveId
        value['sId'] = subobj.sendId
        rUser = self.queryUser(
            {'id': subobj.recieveId}, order_by='id').first()
        sUser = self.queryUser(
            {'id': subobj.sendId}, order_by='id').first()
        if rUser:
            value['rImg'] = settings.MEDIA_URL + str(rUser.uImg)
            value['rName'] = rUser.uName
        value['sImg'] = settings.MEDIA_URL + str(sUser.uImg)
        value['sName'] = sUser.uName
        value['content'] = subobj.messageText.msgContent
        value['time'] = subobj.messageText.msgTime
        return value

    # 获取子评论
    def getChilds(self, parentId, commentId):
        global data
        global item
        sub = {}
        child = []
        if parentId:
            subObjs = msgutil.queryMessage(
                {'recieveId': parentId, 'replyed_messageId': commentId}, connect_type='and', order_by='messageId')
            if subObjs:
                for subobj in subObjs:
                    child.append(self.generateComment_Data(subobj))
                sub[commentId] = child
                item.append(sub)
                for ssub in subObjs:
                    return self.getChilds(ssub.sendId, ssub.messageId)
                data.append(item)

    def load_feedBack(self):
        global data
        global item
        data = []
        item = []
        mts = msgutil.queryMessageText(
            {'msgType': '意见反馈'}, order_by='-msgTime')
        if mts:
            for mt in mts:
                ms = mt.message.first()
                recieveId = ms.recieveId
                if not recieveId:
                    item = []
                    item.append({'parent': self.generateComment_Data(ms)})
                    data.append(item)
                    self.getChilds(ms.sendId, ms.messageId)
            return json.dumps(data)
        return []


#         ms = msgutil.queryMessageText({'msgType': '意见反馈'}, order_by='-msgTime')

    # 获取意见反馈数据
#     def load_feedBack(self):
#         mt = msgutil.queryMessageText({'msgType': '意见反馈'}, order_by='-msgTime')
#         data = []
#         if mt:
#             for m in mt:
#                 item = {}
#                 d = []
#                 ms = m.message.first()
#                 item['id'] = ms.mId
#                 item['content'] = m.msgContent
#                 item['time'] = m.msgTime
#                 rId = ms.recieveId
#                 sId = ms.sendId
#                 if rId:
#                     ru = self.queryUser({'id': rId}, order_by='id').first()
#                     item['rImg'] = settings.MEDIA_URL + str(ru.uImg)
#                     item['rName'] = ru.uName
#                     item['rId'] = rId
#                 else:
#                     item['rImg'] = None
#                     item['rName'] = None
#                     item['rId'] = None
#                 if sId:
#                     su = self.queryUser({'id': sId}, order_by='id').first()
#                     item['sImg'] = settings.MEDIA_URL + str(su.uImg)
#                     item['sName'] = su.uName
#                     item['sId'] = sId
#                 data.append(item)
#             return json.dumps(data)
#         return []
