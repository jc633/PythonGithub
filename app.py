from flask import Flask, escape, url_for,render_template,redirect,request,make_response,session,abort,flash
from werkzeug.utils import secure_filename #过滤文件名中的敏感字符
from flask_mail import Message,Mail #导入邮件类、消息类
import os

app = Flask(__name__)
app.secret_key = 'cyf I love you' #session加密
app.config['UPLOAD_FOLDER']= 'media/' #文件上传存储路径
app.config['MAX_CONTENT_PATH'] = 1*1024*1024 #上传文件最大体积，以字节为单位

#邮箱配置
app.config['MAIL_SERVER']='smtp.139.com'  #服务器
app.config['MAIL_PORT'] = 465  #端口
app.config['MAIL_USERNAME'] = 'jxc516@139.com' #用户名
app.config['MAIL_PASSWORD'] = 'jxc@120702mail' #密码
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) #邮件对象

'''热加载html'''
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

'''热加载静态资源，修改缓存时间'''
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 'timedelta(seconds=1)'


@app.route('/index')
def index():
    if 'username' in  session:
        uname = session['username']
        pwd = session['pwd']
    return render_template('index.html',uname = uname,password = pwd)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dealLogin',methods=['POST','GET'])
def dealLogin():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if name == '陈伊凡' and password == 'jxc':
            session['username'] = name
            session['pwd'] = password
            flash('登录成功','error')
            return redirect(url_for('index'))
        else:
            abort(400)
    else:
        name = request.args.get('name')
        return redirect(url_for('index',name=name))

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect('login')

@app.route('/setcookie',methods=['POST','GET'])
#设置cookie
def setCookie():
    if request.method=='POST':
        uname = request.form['username']
        resp = make_response(render_template('temp.html'))
        resp.set_cookie('uId',uname)
        return resp
    else:
        pass

@app.route('/getCookie')
def getCookie():
    name = request.cookies.get('uId')
    return 'Hello,%s' % name

@app.route('/test')
def test():
    num = 3
    testDict = {'name':'cyf','age':24,'sex':'女'}
    return render_template('test.html',data = num,info = testDict)

@app.route('/user/<username>')
def profile(username):
    return redirect(url_for('hello_cyf',act='love'))

#文件上传测试
@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/dealUpload',methods = ['GET', 'POST'])
def dealUpload():
    if request.method == 'POST':
        img = request.files['uImg']
        savePath = os.path.join(app.config['UPLOAD_FOLDER'],img.filename)
        img.save(savePath)
        return '上传成功！！'
    else:
        pass

#邮件发送
@app.route('/mail')
def ToMail():
    return render_template('sendMail.html')

@app.route('/sendMail',methods=['POST','GET'])
def sendMail():
    if request.method=='POST':
        subject = request.form['subject']
        sendPeople = request.form['sendPeople']
        content = request.form['content']
        msg = Message(subject=subject,recipients=[sendPeople],body=content,sender='jxc516@139.com')
        mail.send(msg)
        return '发送成功'
    return '我爱你'

@app.route('/hello_cyf/<act>')
def hello_cyf(act):
    return 'Cyf,I %s' % act+'you'


if __name__ == '__main__':
    app.run(debug=True)