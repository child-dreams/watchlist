from flask import Flask
from flask import escape
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hao')
def hello():
	return '<h1>Hello haohao!</h1><img src="http://helloflask.com/tutorial.gif">'
@app.route('/user/<name>')
def user_page(name):
	return 'User: %s' % escape(name)

name = 'Hao Hao'
movies = [
	{'title': 'My Neighbor Totoro', 'year': '1988'},
	{'title': 'Love', 'year': '2009'},
	{'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
    	{'title': 'Mahjong', 'year': '1996'},
    	{'title': 'Swallowtail Butterfly', 'year': '1996'},
    	{'title': 'King of Comedy', 'year': '1999'},
    	{'title': 'Devils on the Doorstep', 'year': '1999'},
    	{'title': 'WALL-E', 'year': '2008'},
    	{'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
	return render_template('index.html', name=name, movies=movies)
