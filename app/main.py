from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title="BE-01 Build your first CRUD API",
    description="This is the first API for my Backend AI Internship at FlyRank.",
)

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "done": False
    },
    {
        "id": 3,
        "title": "Submit assignment",
        "done": True
    }
]

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task {task_id} not found"
        )
    return task

@app.get("/health")
def health():
    return {
        "status": "ok"
    }