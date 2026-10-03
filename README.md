# AI-Based Student Skill Gap Analyzer

Pure HTML + CSS + JavaScript frontend with Python FastAPI backend.

## Stack
- Frontend: HTML5, CSS3, Vanilla JavaScript
- Backend: Python + FastAPI
- Database: SQLite locally / PostgreSQL for AWS RDS
- AI: Amazon Bedrock (integration-ready)
- Cloud: AWS
- Infrastructure: Terraform (later stage)
- CI/CD: GitHub Actions (later stage)

## Run frontend
Open `frontend/index.html` directly in a browser, or serve it:

```bash
cd frontend
python3 -m http.server 5500
```

Open http://127.0.0.1:5500

## Run backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs

The frontend uses `http://127.0.0.1:8000/api` by default.
