from flask import Flask,render_template,request,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
import datetime
import sqlite3
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__,  static_url_path='/static')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'Nur'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/C/Users/User/Documents/todo.db'
#
# db = SQLAlchemy(app)
#
# class User(db.Model):
#
#     id = db.Column(db.Integer, primary_key=True)
#     public_id= db.Column(db.String(50), unique=True)
#     name=db.Column(db.String(50))
#     password= db.Column(db.String)
#     admin=db.Column(db.Boolean)
#
# class Todo(db.Model):
#
#     id=db.Column(db.Integer,primary_key=True
#     text=db.Column(db.String(50))
#     complete=db.column(db.Boolean)
#     user_id=db.column(db.Integer)
db_path = r'C:\Users\User\Documents\test.db'

@app.route('/login',methods=['GET','POST'])
def login():
    form=request.form
    if request.method == 'POST':
        name=request.form['username']

        return render_template('index.html')

    return render_template('login.html', form=form)

@app.route('/protected')
def protected():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS user1
                     (id integer PRIMARY KEY ,
                     public_id varchar(50) NOT NULL ,
                     user_name varchar(50) NOT NULL,
                     password varchar(100) NOT NULL,
                     admin boolean DEFAULT 0);
                     """)
    except:
        pass
    conn.commit()  # commit needed
    c.close()

    return 'created1'
@app.route('/user', methods = ['POST'])
def create_user():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    data= request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    c.execute('''insert into user1(public_id,user_name,password,admin) values(?,?,?,?)''', (str(uuid.uuid4()) ,data['name'],hashed_password,0 ))
    conn.commit()  # commit needed
    c.close()
    return 'User is added'
# def create():
#
#
#
# def insert():
#     c.execute("""INSERT INTO mytable (start, end, score)
#               values(1, 99, 123)""")
#
# def select(verbose=True):
#     sql = "SELECT * FROM mytable"
#     recs = c.execute(sql)
#     if verbose:
#         for row in recs:
#             print(row)



# @app.route('/login')
# def login():
#     auth= request.authorization
#     if auth and auth.password == 'password':
#         token=jwt.encode({'user':auth.username, 'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
#         return jsonify({'token': token.decode('UTF-8')})
#     return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm= "Login Required"'})



@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def home1():
    return 'About lesson!'

if __name__ == '__main__':
    app.run(debug=True)



