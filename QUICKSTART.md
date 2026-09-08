# Quick Start Guide - BBQ Restaurant AI Dashboard

## Prerequisites
- Python 3.11+ with pip
- Node.js 16+ with npm
- SQLite3 (included with Python)

## Project Structure
```
restaurant/
├── backend/           # FastAPI server
│   ├── .venv/        # Python virtual environment
│   ├── app/          # Main application code
│   ├── data/         # SQLite database
│   ├── requirements.txt
│   └── .env          # Environment config
├── frontend/         # React + Vite app
│   ├── src/
│   ├── package.json
│   └── .env          # Environment config
└── data/
    └── bbq.db        # Restaurant dataset (3.8 MB)
```

## Setup & Running

### Option 1: Using the Batch Script (Windows)
```bash
# From the project root, double-click:
start-servers.bat

# This will:
# 1. Start backend on http://localhost:8000
# 2. Start frontend on http://localhost:3000
# 3. Open dashboard in browser
```

### Option 2: Manual Setup

#### Backend (Python/FastAPI)
```bash
cd backend

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies (if needed)
pip install -r requirements.txt

# Start the server
python -m uvicorn app.main:app --reload --port 8000
```

Backend will be at: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

#### Frontend (React/Vite)
```bash
cd frontend

# Install dependencies (if needed)
npm install

# Start dev server
npm run dev
```

Frontend will be at: `http://localhost:3000`

## Login

### Demo Mode (Recommended for Testing)
- Click "Try Demo" button if available
- This creates a temporary demo session

### Standard Login
If demo mode is disabled:
- **Username**: `demo`
- **Password**: (check backend console or database)

To create a new user, run from backend directory:
```bash
python scripts/create_user.py --username myuser --password mypass --email myuser@example.com
```

## Dashboard Features

### 📊 Overview
- Key Performance Indicators (KPIs)
- Total Revenue, Orders, Average Order Value
- Gross Profit and Margin percentage
- Monthly revenue trends

### 📈 Analytics
- Sales by branch
- Weekend vs. weekday comparison
- Monthly comparison
- Daily revenue trends

### 🍖 Products
- Top 10 products by revenue
- Product category breakdown
- Product performance metrics

### 🔮 Forecasting
- Revenue forecasts
- Trend analysis
- Best performing days

### 🚨 Alerts & Anomaly Monitoring
- Real-time anomaly detection
- Revenue spike/drop alerts
- Configurable sensitivity levels
- Severity classification (HIGH/MEDIUM)

### 🤖 AI Assistant
- Natural language queries
- Instant analytics answers
- SQL generation and display
- Demo questions provided

## Environment Variables

### Backend (.env in `/backend`)
```env
APP_ENV=development              # development or production
BBQ_DATA_DIR=./data             # Dataset directory
BBQ_DB_PATH=./data/bbq.db       # SQLite database path
JWT_SECRET_KEY=<48+ chars>      # Authentication secret
ACCESS_TOKEN_EXPIRE_MINUTES=60  # Token lifetime
CORS_ORIGINS=http://localhost:3000
DEMO_MODE=false                 # Enable demo login
LLM_PROVIDER=off                # AI backend (off/groq/anthropic)
GROQ_API_KEY=                   # Groq API key (if using Groq)
ANTHROPIC_API_KEY=              # Anthropic key (if using Claude)
```

### Frontend (.env in `/frontend`)
```env
VITE_API_URL=/api               # API base URL (proxied locally)
VITE_DEMO_MODE=false            # Show demo button
```

## Data

### Database: `data/bbq.db`
SQLite database with 5 tables:

| Table | Records | Purpose |
|-------|---------|---------|
| branches | ~10 | Store locations |
| products | ~50 | Menu items |
| customers | ~1000 | Customer records |
| orders | ~10,000 | Order history |
| order_items | ~30,000 | Order line items |

**Date Range**: Historical sales data (configurable by dataset)
**Currency**: PKR (Pakistani Rupees)

To view data directly:
```bash
# Install sqlite3 command line if needed
sqlite3 data/bbq.db

# Example queries:
SELECT COUNT(*) FROM orders;
SELECT SUM(total_amount) FROM orders;
SELECT * FROM branches;
```

## Troubleshooting

### Backend won't start
```
Error: Database not found
→ Ensure data/bbq.db exists
→ Run: python scripts/load_data.py
```

### Frontend shows blank dashboard
```
→ Check browser console (F12)
→ Check Network tab for 404/401 errors
→ Verify backend is running on port 8000
→ Verify API calls include /v1/ prefix
```

### "Authentication required" error
```
→ Login first or use demo mode
→ Check JWT_SECRET_KEY in .env
```

### CORS errors
```
→ Verify CORS_ORIGINS includes your frontend URL
→ Default: http://localhost:3000
```

### Port already in use
```
# Backend (8000):
lsof -i :8000  # List process
kill -9 <PID>  # Kill process

# Frontend (3000):
lsof -i :3000
kill -9 <PID>
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/demo` - Demo access

### Dashboard
- `GET /api/v1/dashboard/kpis` - Key metrics
- `GET /api/v1/anomalies` - Anomaly detection

### Sales
- `GET /api/v1/sales/monthly` - Monthly revenue
- `GET /api/v1/sales/daily` - Daily revenue
- `GET /api/v1/sales/by-branch` - Branch comparison
- `GET /api/v1/sales/best-day` - Top performing day
- `GET /api/v1/sales/weekend-vs-weekday` - Weekend analysis
- `GET /api/v1/sales/month-compare` - Month comparison

### Products
- `GET /api/v1/products/top` - Top products
- `GET /api/v1/products/categories` - Category breakdown

### AI Assistant
- `POST /api/v1/ai/chat` - Natural language queries

### Meta
- `GET /health` - Health status

## Performance Tips

1. **First Load**: Dashboard may take a few seconds to load data
2. **Charts**: Throttle frequent refreshes
3. **Database**: Queries are optimized with indexes
4. **AI**: Set `LLM_PROVIDER=off` to disable AI and reduce overhead

## Support

For issues or questions:
1. Check logs in terminal windows
2. Review browser console (F12)
3. Check `DATASET_FIX_SUMMARY.md` for recent fixes
4. Verify `.env` files are configured correctly

---

**Last Updated**: 2026-09-08
**Status**: ✅ Data loading fixed - All API paths now include `/v1/` prefix

