from action import app
from action.controller import usercontroller
user = usercontroller()
from flask import render_template, request, redirect, url_for, jsonify, make_response
from werkzeug.security import  check_password_hash
import jwt
import datetime

@app.route('/newuser', methods=['POST'])
def adduser():
    try:
        data = request.get_json(force=True, silent=True)
    except:
        return 'Error!'
    response = user.adduser(data)
    return response
from functools import wraps
def token_required(f):
     @wraps(f)
     def decorated(*args, **kwargs):
         token= None
         refresh_token=None
         if 'Cookie' in request.headers:
             token = request.cookies.get('x-access-token')
             refresh_token = request.cookies.get('x-refresh-token')
         if not token and not refresh_token:
                return 'token is missing',401
         try:
             data = jwt.decode(token, app.config['SECRET_KEY'])
             current_user = user.get_bypId(data['public_id'])
         except:
            try:
             data = jwt.decode(refresh_token, app.config['SECRET_KEY'])
             current_user = user.get_bypId(data['public_id'])
             token = jwt.encode({'public_id': current_user['data'][0][1], 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3)},app.config['SECRET_KEY'])
            except:
                return 'token is invalid', 401

         return f(current_user,token, *args, **kwargs)
     return decorated

@app.route('/', methods=['GET', 'POST'])
def login():
    form = request.form
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        user_info = user.get_byname(name)
        if user_info['code'] != 200:
            return render_template('login.html', form=form, info="Неправильный логин или пароль...")
        elif check_password_hash(user_info['data'][0][3], password):
            token = jwt.encode({'public_id': user_info['data'][0][1], 'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=15)}, app.config['SECRET_KEY'])
            refresh_token=jwt.encode({'public_id': user_info['data'][0][1], 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=2)}, app.config['SECRET_KEY'])
            print(refresh_token)
            resp = make_response(redirect(url_for('logged', public_Id=user_info['data'][0][1])))
            resp.set_cookie('x-access-token', token)
            resp.set_cookie('x-refresh-token', refresh_token)
            return resp
        else:
            return render_template('login.html', form=form, info="Неправильный логин или пароль...", user="nurik")
    return render_template('login.html', form=form)

@app.route('/logged/<public_Id>', methods=['GET'])
@token_required
def logged(current_user, token, public_Id):
    resp=make_response(render_template('index.html'))
    resp.set_cookie('x-access-token', token)
    return resp

@app.route('/logout', methods=['GET'])
@token_required
def logout(current_user, token):
    resp=make_response(redirect('/'))
    resp.set_cookie('x-access-token', expires=0)
    resp.set_cookie('x-refresh-token', expires=0)
    return resp