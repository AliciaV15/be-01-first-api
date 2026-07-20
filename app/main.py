from fastapi import FastAPI, HTTPException, Response, status

app = FastAPI(
    title="BE-01 Build your first CRUD API",
    description="This is the first API for my Backend AI Internship at FlyRank.",
)

initial_tasks  = [
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

tasks = initial_tasks.copy()

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

#EXTRAS  
@app.get("/tasks/done")
def get_done_tasks(done: bool):
    filtered_tasks = [task for task in tasks if task["done"] == done]
    return filtered_tasks

@app.get("/tasks/search")
def search_tasks(title: str):
    filtered_tasks = [task for task in tasks if title.lower() in task["title"].lower()]
    return filtered_tasks

@app.get("/stats")
def get_stats():
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task["done"]])
    pending_tasks = total_tasks - completed_tasks
    
    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks
    }

@app.post("/reset")
def reset_tasks():
    global tasks
    tasks = [task.copy() for task in initial_tasks]
    return {"message": "Tasks have been reset to the initial state."}

#CRUD
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
        "id": max(task["id"] for task in tasks) + 1 if tasks else 1,
        "title": title,
        "done": False
    }
    
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={"error": "Request body is required"}
        )
        
    for task in tasks:
        if task["id"] == task_id:
            if "title" in updated_task:
                if not updated_task["title"].strip():
                   raise HTTPException(
                       status_code=status.HTTP_400_BAD_REQUEST, 
                       detail={"error": "Title cannot be empty"}
                   )
                task["title"] = updated_task["title"]
                
            if "done" in updated_task:
                task["done"] = updated_task["done"]
            return task
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )

@app.delete ("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
    raise HTTPException(
        status_code=404,
        detail={"error": f"Task {task_id} not found"}
    )
    
#EXTRAS




@app.get("/health")
def health():
    return {
        "status": "ok"
    }