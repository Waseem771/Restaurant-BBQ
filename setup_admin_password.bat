@echo off
REM Setup Admin Password
REM Username: admin
REM Password: iba@12345admin (14 characters - meets 12+ requirement)

echo.
echo ================================================
echo   Setting Up Admin User
echo ================================================
echo.

cd /d "%~dp0backend"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the script to setup admin
python setup_admin_password.py

echo.
echo ================================================
echo   Admin User Ready to Use
echo ================================================
echo.
pause
