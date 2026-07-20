from fastapi import FastAPI 

app = FastAPI(
    title="BE-01 Build your first CRUD API",
    description="This is the first API for my Backend AI Internship at FlyRank.",
)

@app.get("/")
def root():
    return {"message": "Hello, Backend AI Engineering!"}