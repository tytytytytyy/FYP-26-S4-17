# Human-in-the-Loop Intrusion Detection Dashboard

FYP-26-S4-17 (UOW CSCI321 / CSIT321 at SIM).

A sensor captures live network traffic with CICFlowMeter and sends flow records to a FastAPI backend.
ML models (Random Forest + Isolation Forest) score each flow and raise alerts, which appear live on a
React dashboard over WebSocket. Analysts close alerts as True Positive, Benign Positive or False Positive,
and those labels are used to retrain the model.

## Folders

| Folder | What lives here | Package owner |
| --- | --- | --- |
| `backend/` | FastAPI API, database models, WebSocket alerts | A (Tai), D (Mahalakshmi) |
| `frontend/` | React + Vite dashboard | E (Jerome), D (Mahalakshmi) |
| `sensor/` | Sensor agent (CICFlowMeter capture, heartbeat, buffer) | B (Leika) |
| `ml/` | Training, scoring and retraining code, notebooks | C (Khalis) |
| `docs/` | Agreed formats, design notes | Everyone |
| `marketing/` | Public marketing site (plain HTML/CSS), deployed to GitHub Pages | Everyone |

The marketing site deploys automatically when `marketing/` changes on `main`:
https://tytytytytyy.github.io/FYP-26-S4-17/

## Run it locally

You need Python 3.12, Node.js (current LTS) and Docker Desktop.

```bash
# 1. Database (Postgres in Docker)
docker compose up -d db

# 2. Backend
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate    Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://localhost:8000/docs

# 3. Frontend (new terminal)
cd frontend
npm install
npm run dev
# open http://localhost:5173
```

Copy `.env.example` to `.env` before running. Never commit `.env`.

## How we work

1. Each Taiga story gets its own branch, named after the story, e.g. `B-sensor-agent`.
2. Push the branch and open a pull request into `main`.
3. CI (GitHub Actions) must pass, and one teammate must approve.
4. Move the Taiga story to Ready for test. The reviewer moves it to Done.

Nobody pushes straight to `main`, and nobody approves their own pull request.
