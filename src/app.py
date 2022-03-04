from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__) #name es una variable especial que lee el interprete de Python al leer el .py


todos = [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    data = json.loads(request_body)
    todos.append(data)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)


if __name__ == "__main__": #Comprobamos si estamos en el .py principal
    app.run(host='0.0.0.0', port=3245, debug=True)