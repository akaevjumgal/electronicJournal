from action.model import users
from action.model.configs import db_path

userdb= users(db_path)

class usercontroller:
    def adduser(self, data):
        return  userdb.create_user(data)
    def get_byname(self,name):
        return userdb.getByname(name)
    def get_bypId(self,pId):
        return userdb.getBypId(pId)