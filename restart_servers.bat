@echo off
REM Restart BBQ Dashboard - Backend and Frontend
REM This script will restart everything fresh

echo.
echo ================================================
echo   Restarting BBQ Dashboard
echo ================================================
echo.

REM Kill any existing processes on ports 8000 and 3000
echo Cleaning up old processes...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM node.exe >nul 2>&1

echo Waiting for cleanup...
timeout /t 3 /nobreak

echo.
echo ================================================
echo   Starting Backend (FastAPI on port 8000)
echo ================================================
echo.

REM Start Backend in new terminal
start cmd /k "cd /d "%CD%\backend" && .venv\Scripts\activate.bat && python -m uvicorn app.main:app --reload --port 8000"

timeout /t 3 /nobreak

echo.
echo ================================================
echo   Starting Frontend (React on port 3000)
echo ================================================
echo.

REM Start Frontend in new terminal
start cmd /k "cd /d "%CD%\frontend" && npm run dev"

timeout /t 3 /nobreak

echo.
echo ================================================
echo   Servers Starting
echo ================================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Waiting for servers to start (usually 30-60 seconds)...
echo.

REM Wait and then open browser
timeout /t 5 /nobreak

echo Opening dashboard in browser...
start http://localhost:3000

echo.
echo ================================================
echo   Setup Complete
echo ================================================
echo.
echo Backend running on: http://localhost:8000
echo Frontend running on: http://localhost:3000
echo.
echo Login with:
echo   Username: admin
echo   Password: iba@12345678
echo.
pause
