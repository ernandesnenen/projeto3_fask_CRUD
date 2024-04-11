import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

#criar tarefas
def test_create_task():
  new_task_data ={
    "title":"new task",
    "description":"task of test"
  }
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  assert response.status_code == 200
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  tasks.append(response_json['id'])

#recuperar as tarefas
def test_get_tasks(): 
  response = requests.get(f"{BASE_URL}/tasks")
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json

#recupera a tarefa
def test_get_task():
  task_id = tasks[0] 
  response = requests.get(f"{BASE_URL}/tasks/{task_id}")
  assert response.status_code == 200
  response_json = response.json()
  assert task_id == response_json['id']

#update a tarefa
def test_update_task():
  if tasks:
     task_id = tasks[0]
     print(f"task_id::> {task_id}")
     payload = {
      "title":"atualizado",
      "description":"atualizado",
      "completed": True
     }
     response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
     response_json = response.json()
     assert response.status_code == 200
     assert response_json['message'] == "update Task success"

     dado = requests.get(f"{BASE_URL}/tasks/{task_id}")
     dado_json = dado.json()
     print(f"dados::> {dado_json}")
     assert dado_json["title"] == payload["title"]
     assert dado_json["description"] == payload["description"]
     assert dado_json["completed"] == payload["completed"]
     
#delete a tarefa
def test_delete_task():
  if tasks:
     task_id = tasks[0]
     print(f"task_id::> {task_id}")
     response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
     response_json = response.json()
     assert response_json['message'] == "Task deleted success"
     assert response.status_code == 200
     response = requests.get(f"{BASE_URL}/tasks/{task_id}")
     assert response.status_code == 404
 
  
