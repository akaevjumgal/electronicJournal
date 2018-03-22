from action import app
from action.controller import usercontroller
from flask import request
user= usercontroller()

@app.route('/user', methods=['POST'])
def adduser():
    try:
        data = request.get_json(force=True, silent=True)
    except:
        return 'Error!'
    response = user.adduser(data)
    return response
