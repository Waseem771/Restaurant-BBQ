@echo off
REM Add Waseem user to BBQ Dashboard
REM Password requirement: minimum 12 characters

echo.
echo ================================================
echo   Adding Waseem User to Dashboard
echo ================================================
echo.

cd /d "%~dp0backend"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the script to add user
python add_waseem_user.py

echo.
echo ================================================
echo   User Creation Complete
echo ================================================
echo.
echo You can now login with:
echo   Username: waseem
echo   Password: iba@123waseem
echo.
pause
