@echo off
REM Fix Admin Login - Create admin with password iba@12345678

echo.
echo ================================================
echo   Fixing Admin Login
echo ================================================
echo.

cd /d "%~dp0backend"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the script to fix admin
python fix_admin_login.py

echo.
echo ================================================
echo   Admin User Fixed
echo ================================================
echo.
echo Now run: start-servers.bat
echo Then login with:
echo   Username: admin
echo   Password: iba@12345678
echo.
pause
