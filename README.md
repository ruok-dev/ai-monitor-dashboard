# AI Monitor Dashboard 🚀

A high-performance monitoring dashboard with real-time alerts, structured logging, and ML-driven anomaly detection. Built with **FastAPI**, **React**, and **PostgreSQL**.

## Features

-   **Real-time Monitoring**: Live log streaming via WebSockets.
-   **AI Anomaly Detection**: ML service (Isolation Forest) to detect unusual patterns in logs.
-   **Structured Logging**: Comprehensive log metadata and filtering.
-   **Security First**:
    -   JWT-based authentication.
    -   Secure environment variable management.
    -   Sensitive data protected from Git (pre-configured `.gitignore`).
-   **Premium Design**: Modern UI with glassmorphism, HSL color palettes, and responsive layout.

## Project Structure

```
├── backend/            # FastAPI Application
│   ├── app/
│   │   ├── api/        # API Endpoints
│   │   ├── core/       # Config & Security
│   │   ├── db/         # Database Session
│   │   ├── models/     # SQLModels (SQLAlchemy)
│   │   ├── services/   # Business Logic (ML, WebSockets)
│   ├── run.py          # Runner script
├── frontend/           # React Application (Vite)
│   ├── src/
│   │   ├── components/ # Reusable UI
│   │   ├── App.jsx     # Main entry
├── scripts/            # Utility & Simulation scripts
└── .env.example        # Environment variables template
```

## Getting Started

### 1. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp ../.env.example .env
python run.py
```

### 2. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

### 3. Run Simulation

```bash
python scripts/simulate_logs.py
```

## Security Note

Always ensure `.env` is listed in your `.gitignore` before pushing to GitHub. Never commit your `SECRET_KEY` or database credentials.
