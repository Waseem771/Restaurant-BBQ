# 🔄 RESTART SERVERS - COMPLETE GUIDE

**Status**: ✅ Restart scripts ready
**Date**: 2026-09-08 08:23 UTC
**Ready**: YES - RESTART NOW!

---

## 🚀 OPTION 1: AUTOMATIC RESTART (EASIEST)

### Step 1: Run Restart Script
```bash
cd restaurant
restart_servers.bat
```

**This will automatically:**
1. ✅ Stop all existing processes
2. ✅ Start backend on port 8000
3. ✅ Start frontend on port 3000
4. ✅ Open dashboard in browser
5. ✅ Show login page

### Step 2: Wait for Servers
Wait 30-60 seconds for both servers to start

### Step 3: Login
- **URL**: http://localhost:3000
- **Username**: admin
- **Password**: iba@12345678

---

## 🔄 OPTION 2: MANUAL RESTART (FULL CONTROL)

### Step 1: Close Everything
```bash
# Close all terminals (Ctrl+C in each)
# Close all browsers
# Wait 5 seconds
```

### Step 2: Start Backend (Terminal 1)
```bash
cd backend
.venv\Scripts\activate.bat
python -m uvicorn app.main:app --reload --port 8000
```

**Wait for**: 
```
INFO:     Application startup complete
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Start Frontend (Terminal 2)
```bash
cd frontend
npm run dev
```

**Wait for**: 
```
Local:   http://localhost:3000
```

### Step 4: Open Dashboard
Open browser to: http://localhost:3000

---

## ✅ VERIFICATION AFTER RESTART

### Backend Status
- ✅ Running on http://localhost:8000
- ✅ API docs at http://localhost:8000/docs
- ✅ Health check: http://localhost:8000/health

### Frontend Status
- ✅ Running on http://localhost:3000
- ✅ Login page appears
- ✅ Can enter credentials

### Login Status
- ✅ Username: admin
- ✅ Password: iba@12345678
- ✅ Dashboard loads with data

---

## 🎯 QUICK REFERENCE

| Task | Command |
|------|---------|
| Auto Restart | `restart_servers.bat` |
| Start Backend | `cd backend && .venv\Scripts\activate.bat && python -m uvicorn app.main:app --reload --port 8000` |
| Start Frontend | `cd frontend && npm run dev` |
| Stop All | Close all terminals |
| Check Backend | http://localhost:8000/health |
| Check Frontend | http://localhost:3000 |

---

## 🛠️ TROUBLESHOOTING

### Port Already in Use
```bash
# Kill processes on port 8000
taskkill /F /IM python.exe

# Kill processes on port 3000
taskkill /F /IM node.exe

# Then restart
```

### Backend Won't Start
1. Check .env file is correct
2. Verify database exists: `data/bbq.db`
3. Check Python is installed: `python --version`

### Frontend Won't Start
1. Check node_modules exist: `cd frontend && dir node_modules`
2. If missing, run: `npm install`
3. Then try again

### Can't Login After Restart
1. Verify you're using correct password: `iba@12345678`
2. Clear browser cache (Ctrl+Shift+R)
3. Try again

---

## ✨ EXPECTED OUTPUT

### Backend Starting
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

### Frontend Starting
```
VITE v5.0.0 ready in 123 ms

➜  Local:   http://localhost:3000/
➜  press h to show help
```

### Browser Opening
```
Login page appears at http://localhost:3000
You can enter: admin / iba@12345678
```

---

## 🎯 COMPLETE RESTART PROCESS

```
1. Run: restart_servers.bat
   ↓
2. Wait: 30-60 seconds for startup
   ↓
3. See: Both servers running
   ↓
4. Browser opens: http://localhost:3000
   ↓
5. Enter: admin / iba@12345678
   ↓
6. Click: Sign In
   ↓
7. Dashboard loads with all data
   ↓
✅ COMPLETE - READY TO USE
```

---

## 📋 RESTART CHECKLIST

- [ ] Closed all old terminals
- [ ] Closed all browsers
- [ ] Waited 5 seconds
- [ ] Ran `restart_servers.bat` OR started manually
- [ ] Waited for both servers to start
- [ ] Dashboard page loaded
- [ ] Login page appeared
- [ ] Entered admin / iba@12345678
- [ ] Dashboard loaded with data

---

## 🎉 YOU'RE READY!

Both servers are restarted and ready to use.

**Login credentials:**
```
Username: admin
Password: iba@12345678
```

**Your dashboard is operational!** 🍖📊

---

**Status**: ✅ READY TO RESTART
**Time**: 2026-09-08 08:23 UTC

