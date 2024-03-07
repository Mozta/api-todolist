from flask import Flask, jsonify, request, abort
from datetime import datetime

app = Flask(__name__)

tasks = [
    {
        "category": "Comida",
        "created": "Mon, 04 Mar 2024 18:02:12 GMT",
        "id": 1,
        "name": "Comer",
        "status": False,
        "updated": "Mon, 04 Mar 2024 18:02:12 GMT"
    },
    {
        "category": "Escuela",
        "created": "Mon, 04 Mar 2024 18:02:14 GMT",
        "id": 2,
        "name": "Dar la clase",
        "status": False,
        "updated": "Mon, 04 Mar 2024 18:02:14 GMT"
    }
]

BASE_URL = '/api/v1/'


@app.route('/')
def home():
    return '<h1>Welcome to my first api deploy</h1>'


@app.route(BASE_URL + 'tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400, error='Missing body in request')
    this_time = datetime.now()
    task = {
        'id': len(tasks) + 1,
        'name': request.json['name'],
        'category': request.json['category'],
        'status': False,
        'created': this_time,
        'updated': this_time,
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route(BASE_URL + 'tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route(BASE_URL + 'tasks/<int:id>', methods=['GET'])
def get_task(id):
    this_task = [task for task in tasks if task['id'] == id]
    print("TASK")
    if len(this_task) == 0:
        abort(404, error='ID not found!')
    return jsonify({'task': this_task[0]})


@app.route(BASE_URL + 'tasks/<int:id>', methods=['PUT'])
def check_task(id):
    this_task = [task for task in tasks if task['id'] == id]
    if len(this_task) == 0:
        abort(404, error='ID not found!')
    this_task[0]['status'] = not this_task[0]['status']
    return jsonify({'task': this_task[0]})

@app.route(BASE_URL + 'tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    this_task = [task for task in tasks if task['id'] == id]
    if len(this_task) == 0:
        abort(404, error='ID not found!')
    tasks.remove(this_task[0])
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run(debug=False)
