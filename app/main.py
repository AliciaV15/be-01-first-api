from fastapi import FastAPI 

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



@app.get("/health")
def health():
    return {
        "status": "ok"
    }