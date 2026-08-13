
# Mini Task Queue

## Goal

Build a simple backend task queue to understand how background workers process tasks separately from API requests.

## Basic Workflow

---
```text
Client
   |
   | POST /tasks
   v
FastAPI
   |
   | add task
   v
Task Queue
   |
   v
Worker
   |
   | process task
   v
Completed
```
---

## Main Components

### FastAPI

Receives requests from the client and puts tasks into the queue.

### Task Queue

Temporarily stores tasks waiting to be processed.

For the first version, the queue will exist in memory using Python's `queue.Queue`.

### Worker

Continuously checks the queue, takes available tasks, and processes them.

## First Version

The first version will support:

---
```text
POST /tasks
```
---

The API will:

1. Receive a task.
2. Validate the request.
3. Add the task to the queue.
4. Return a task ID and queued status.

The worker will:

1. Wait for a task.
2. Take the task from the queue.
3. Process it.
4. Mark the task as completed.

## Libraries

---
```text
FastAPI      → API
Uvicorn      → ASGI server
Pydantic     → request validation
queue        → in-memory task queue
threading    → worker execution
time         → simulate task processing
```
---

`queue`, `threading`, and `time` are Python standard-library modules and do not need to be installed.








Status: Planned
Next: Implement the in-memory queue and first worker.


