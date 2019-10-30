from flask import Flask, escape, url_for,render_template,redirect,request,make_response


app = Flask(__name__)

'''热加载html'''
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/index/<name>')
def index(name):
    return render_template('index.html',name=name)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dealLogin',methods=['POST','GET'])
def dealLogin():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return render_template('index.html',name=name,password=password)
    else:
        name = request.args.get('name')
        return redirect(url_for('index',name=name))

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

@app.route('/hello_cyf/<act>')
def hello_cyf(act):
    return 'Cyf,I %s' % act+'you'


if __name__ == '__main__':
    app.run(debug=True)