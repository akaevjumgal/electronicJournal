from action import app
from action.view  import user
from flask import render_template,request,redirect,url_for
from action.controller import usercontroller
from werkzeug.security import  check_password_hash,generate_password_hash
import jwt
import datetime
from functools import wraps

user=usercontroller()
def token_required(f):
     @wraps(f)
     def decorated(*args, **kwargs):
         token= None
         if 'x-access-token' in request.headers:
             token = request.headers['x-access-token']
         if not token:
                return 'token is missing',401
         try:
             data=  jwt.decode(token,app.config['SECRET_KEY'])
             current_user=user.get_bypId(data['public_id'])
         except:
             return 'token is invalid',401
         return f(current_user,*args,**kwargs)
     return decorated

@app.route('/', methods=['GET', 'POST'])
def login():
    form = request.form
    if request.method == 'POST':
        name = request.form['username']
        password=request.form['password']
        user_info = user.get_byname(name)
        print(name)
        if user_info['code'] != 200:
            return render_template('login.html', form=form, info="Неправильный логин или пароль...")

        elif check_password_hash(user_info['data'][0][3], password ):
            # token = jwt.encode({'public_id': user_info['data'][0][1], 'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=30)},app.config['SECRET_KEY'])
            token = request.headers['x-access-token']
            print(token)
            return redirect(url_for('log', token=token))
        else:
            return render_template('login.html', form=form, info="Неправильный логин или пароль...",user="nurik")
    return render_template('login.html', form=form)
@app.route('/usertoken=<string:token>',methods=['GET'])
@token_required
def log(token):

    return 'Привет '+token
