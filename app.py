from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = []
BASE_URL = '/api/v1/'


@app.route('/')
def home():
    return 'Welcome to my To-Do List'


@app.route('/api/v1/tasks', methods=['POST'])
def create_task():
    print("entreee")
    if not request.json:
        print("aaaaaaa")
        return 'aaaaaa'#abort(404)
    print("eeeeee")
    return 'eeeee'


if __name__ == "__main__":
    app.run(debug=True)
