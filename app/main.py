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

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: dict):
    title = task.get("title")
    
    if not title or not title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={"error": "Title is required"}
        )
    
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    
    tasks.append(new_task)
    return new_task

@app.get("/health")
def health():
    return {
        "status": "ok"
    }