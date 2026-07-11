from fastapi import FastAPI 

app = FastAPI(
    title="BE-01 First API",
    description="This is the first API for my Backend AI Internship at FlyRank.",
)

@app.get("/")
def root():
     return {
        "assignment": "BE-01",
        "message": "Welcome to my first Backend AI Engineering API!"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "running"
    }