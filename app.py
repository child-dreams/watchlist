from flask import Flask
from flask import escape
app = Flask(__name__)

@app.route('/hao')
def hello():
	return '<h1>Hello haohao!</h1><img src="http://helloflask.com/hoahao.gif">'
@app.route('/user/<name>')
def user_page(name):
	return 'User: %s' % escape(name)
