# Feature Analytics Dashboard

This repository contains a prototype for an AI-powered analytics dashboard. It
includes a React frontend and a FastAPI backend. The backend stores click events
in SQLite and provides aggregated analytics and simple AI insights.

## Project structure

- `backend/` — FastAPI application
- `frontend/` — React TypeScript client
- `ai_service/` — placeholder for advanced AI components
- `db/` — database files

## Setup

1. Install Python dependencies:

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

2. In another terminal, run the frontend:

```bash
cd frontend
npm install
npm start
```

The frontend dev server proxies API requests to the backend.

### Docker

Use `docker-compose` to start everything:

```bash
docker-compose up --build
```

## API

- `POST /api/clicks` — store a click event
- `GET /api/analytics` — aggregated statistics
- `GET /api/insights` — simple AI-generated summary

## Example insight output

```
Top feature 'feature_a' has 120 clicks. Least used feature 'feature_b' has 5 clicks.
```

## Sales data utility

The `add.py` script parses a `salesdata.csv` file and generates several helper
reports:

* `output.csv` and `bargraph.png` — total revenue per product
* `last_30_days.csv` — records from the last 30 days
* `daily.png` — daily revenue plot
* `taxed.csv` — revenue with tax and net calculations
* `summary.csv` — aggregate statistics per product

Run it from the repository root:

```bash
python add.py
```
