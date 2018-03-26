from .db import db
from werkzeug.security import generate_password_hash
import uuid
import sqlite3
from action.model.configs import db_path
import json

class users(db):
    def create_user(self, data):

        # conn = sqlite3.connect(db_path)
        # c = conn.cursor()
        # try:
        #     c.execute("""CREATE TABLE IF NOT EXISTS user
        #                      (id integer PRIMARY KEY ,
        #                      public_id varchar(50) NOT NULL ,
        #                      user_name varchar(50) NOT NULL,
        #                      password varchar(100) NOT NULL,
        #                      admin boolean DEFAULT 0);
        #                      """)
        # except:
        #     pass
        # conn.commit()  # commit needed
        # c.close()

        print(data)
        sql='''insert into user
        (public_id,user_name,password,admin)
         values(?,?,?,?)'''
        hashed_password = generate_password_hash(data['password'], method='sha256')
        params=(str(uuid.uuid4()), data['name'], hashed_password, 0)
        self.create_conn()

        created = self.do(sql,params=params,commit=True)
        if created['code'] !=200:
            self.close_conn()
            return created
        self.close_conn()
        return 'User is added'

    def getByname(self, name):
        sql = '''
            select
                id,
                public_id,
                user_name,
                password,
                admin
            from user
            where user_name = ?
        '''
        self.create_conn()
        sql_data = self.do(sql, params=(name,), out=True)
        self.close_conn()
        return sql_data
    def getBypId(self, pId):
        sql = '''
            select
                id,
                public_id,
                user_name,
                password,
                admin
            from user
            where public_id = ?
        '''
        self.create_conn()
        sql_data = self.do(sql, params=(pId,), out=True)
        self.close_conn()
        return sql_data
