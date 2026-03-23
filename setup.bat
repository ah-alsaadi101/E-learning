@echo off
REM E-Learning Platform - Setup Script for Windows
REM This script automates the initial setup process

echo.
echo ==========================================
echo E-Learning Platform - Setup Script
echo ==========================================
echo.

REM Check Python version
echo [*] Checking Python version...
python --version
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo [*] Creating virtual environment...
    python -m venv venv
    echo     Virtual environment created
) else (
    echo [*] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip setuptools wheel
echo.

REM Install requirements
echo [*] Installing requirements...
pip install -r requirements.txt
echo.

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo [*] Creating .env file...
    copy .env.example .env
    echo     .env file created - please update with your settings
) else (
    echo [*] .env file already exists
)
echo.

REM Create logs directory
echo [*] Creating logs directory...
if not exist "logs" mkdir logs
echo.

REM Run migrations
echo [*] Running database migrations...
python manage.py migrate
echo.

REM Create superuser
echo [*] Creating superuser account...
echo     Please enter superuser credentials:
python manage.py createsuperuser
echo.

REM Collect static files
echo [*] Collecting static files...
python manage.py collectstatic --noinput
echo.

echo ==========================================
echo [OK] Setup Complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Review and update .env file settings
echo 2. Run: python manage.py runserver
echo 3. Access: http://localhost:8000
echo 4. Admin: http://localhost:8000/admin
echo.
echo For more information, see README.md
echo.
pause