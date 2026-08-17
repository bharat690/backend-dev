from fastapi import FastAPI , HTTPException
from queue import Queue , Empty

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
    try:
        task = my_queue.get_nowait()
    except Empty:
        raise HTTPException(
            status_code=404,
            detail="No Tasks Remaining in Queue"
        )