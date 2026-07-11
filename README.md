# BE-01 – First API Endpoint

This project was created as part of the **FlyRank Backend AI Engineering Internship**.

The goal of this assignment is to build a minimal backend server with two JSON endpoints, understand the request-response cycle, and publish the project to GitHub.

## Technologies

- Python
- FastAPI
- Uvicorn

## Project Structure

```
be-01-first-api/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/ (not tracked)
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AliciaV15/be-01-first-api.git
cd be-01-first-api
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

The server will be available at:

```
http://127.0.0.1:8000
```

## Available Endpoints

### GET /

Returns a welcome message.

```json
{
  "message": "Hello, Backend AI Engineering!"
}
```

### GET /health

Returns the API health status.

```json
{
  "status": "ok"
}
```

---
**FlyRank Backend AI Engineering Internship – Assignment BE-01**# be-01-first-api
