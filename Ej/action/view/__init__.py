from action import app
from action.view  import user
from flask import jsonify

@app.route('/datatable',methods=['GET'])

def jsony():

    return jsonify({"data":[
        [
         "Абакиров",
         "фывфыв",
         "456"
         ],
        [
            "Абакиров",
            "фывфыв",
            "456"
        ],
        [
            "Абакиров",
            "фывфыв",
            "456"
        ]
    ]})
