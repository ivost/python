import requests
from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app

url = 'https://jsonplaceholder.typicode.com'


@app.route('/')
@app.route('/index')
def index():
    print('INDEX')
    user = {'nickname': 'Ivo'}
    r = requests.get(url + '/posts')
    print('status', r.status_code)
    if r.status_code == 200:
        return render_template('index.html',
                                     title='Home',
                                     user=user,
                                     posts=r.json())


@app.route('/configure', methods=['GET', 'POST'])
def config():
    print('CONFIG')
    form = LoginForm()
    if form.validate_on_submit():
        print("Name", form.name.data)
        flash('Login requested for name="%s", remember_me=%s' %
              (form.name.data, str(form.remember_me.data)))

        return redirect('/index')
    return render_template('config.html',
                                 title='Configuration',
                                 form=form)
