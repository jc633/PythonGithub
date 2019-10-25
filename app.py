from flask import Flask, escape, url_for,render_template,redirect


app = Flask(__name__)

'''热加载html'''
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login/<int:id>')
def login(id):
    return render_template('login.html')

@app.route('/user/<username>')
def profile(username):
    return redirect(url_for('hello_cyf',act='love'))

@app.route('/hello_cyf/<act>')
def hello_cyf(act):
    return 'Cyf,I %s' % act+'you'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login',id=3))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True)