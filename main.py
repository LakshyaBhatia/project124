from flask import Flask,jsonify,request
app=Flask(__name__)

tasks = [
    {
        'id':1,
        'name':u'xyz',
        'contactNumber':u'10000000000000000000000',
        'done':False
    },
    {
        'id':2,
        'name':u'abc',
        'contactNumber':u'10000000000000000000000000000000000000000000',
        'done':False
    },
]


@app.route("/")
def hello_world():
    return "hello world"
@app.route("/get-data")
def hello():
    return jsonify({
         "data":tasks
    })

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'description': request.json.get('contactNumber', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!",
        # added to show all tasks added by me
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug=True)

