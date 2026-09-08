@echo off
REM Create Admin user for BBQ Dashboard
REM Username: admin
REM Password: iba@123admin (12 characters - meets requirement)

echo.
echo ================================================
echo   Creating Admin User
echo ================================================
echo.

cd /d "%~dp0backend"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the script to create admin
python create_admin.py

echo.
echo ================================================
echo   Admin User Ready
echo ================================================
echo.
pause
