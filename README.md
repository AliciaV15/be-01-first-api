# BE-01 – Task CRUD API

This project was developed as part of the **FlyRank Backend AI Engineering Internship**.

It implements a REST API for managing a to-do list using FastAPI. The application stores data in memory and supports full CRUD operations, automatic API documentation with Swagger UI, and a few optional features such as filtering, searching, and task statistics.

---

## Technologies

- Python 3
- FastAPI
- Uvicorn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/AliciaV15/be-01-task-api.git
cd be-01-task-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |
| GET | `/tasks/done?done=true` | Filter tasks by completion status |
| GET | `/tasks/search?query=text` | Search tasks by title  |
| GET | `/stats` | Task statistics  |
| POST | `/reset` | Restore sample tasks  |

---

## Example curl

Create a task:

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Buy milk\"}"
```

Example response:

```http
HTTP/1.1 201 Created

{
    "id": 4,
    "title": "Buy milk",
    "done": false
}
```

---

## Swagger UI

> Add a screenshot of `/docs` here.

Example:

```
docs/swagger.png
```

or simply paste the screenshot below this section.

---

## Data Persistence

This project intentionally stores data only in memory.

After restarting the server, all tasks created during execution are lost and only the initial sample tasks remain. This behavior is expected because no database is used yet; it prepares the project for the next assignment, where PostgreSQL will replace the in-memory storage.

---

## Optional Features

- Filter tasks by completion status.
- Search tasks by title.
- Task statistics endpoint.
- Reset endpoint for restoring sample tasks.

---


**FlyRank Backend AI Engineering Internship – Assignment BE-01**