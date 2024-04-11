from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)
tasks = []
id_control = 1



@app.route('/tasks', methods=['POST'])
def create_task():
    global id_control #o global é usado aqui porque a variavel se encontra fora do method
    data = request.get_json()
    new_task = Task(id = id_control, title=data.get("title"), description=data.get("description"))
    id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "task registered successfully","id":new_task.id})

@app.route("/tasks" , methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    # for task in tasks:
    #     task_list.append(task.to_dict()) 
    # poderia ser assim támbem

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }

    return jsonify(output)

@app.route("/tasks/<int:id>" , methods=['PUT'])
def update_task(id):  
    data = request.get_json()
    task = None
    for find_task in tasks:
        if find_task.id == id:
            task = find_task
            # break
        if task == None:
            return jsonify({"message": "Task not find"}),404
        
        task.title = data['title']    
        task.description = data['description']    
        task.completed = data['completed']    

        return jsonify({"message": "update Task success"})

@app.route("/tasks/<int:id>" , methods=['GET'])
def get_task(id):
    task = None
    for find_task in tasks:
        if find_task.id == id:
            return jsonify(find_task.to_dict())

    return jsonify({"message": "Task not find"}),404

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_task(id):
    task = None
    for find_task in tasks:
        if find_task.id == id:
            task = find_task
            tasks.remove(task)
            return jsonify({"message":"Task deleted success"})

    return jsonify({"message": "Task not find"}),404





if __name__ == "__main__":
    app.run(debug=True)

