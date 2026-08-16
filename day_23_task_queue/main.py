from fastapi import FastAPI 
from queue import Queue

app = FastAPI()

@app.get("/")
def home():
    return{
        "message":"Connected to Server"
    }
my_queue = Queue()
  
@app.post("/tasks")
def task(tasks: list):
    for task in tasks:
        my_queue.put(task)
    
    return {
    "message": "Tasks queued",
    "count": len(tasks)
    }
    
@app.get("/tasks/next")
def get_next_task():
    task = my_queue.get_nowait()

    return {
        "task": task
    }