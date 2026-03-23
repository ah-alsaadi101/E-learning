#!/bin/bash
# E-Learning Platform - Setup Script
# This script automates the initial setup process

set -e  # Exit on error

echo "=========================================="
echo "E-Learning Platform - Setup Script"
echo "=========================================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python_version=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "  Python version: $python_version"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "✓ Creating virtual environment..."
    python -m venv venv
    echo "  Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate  # Linux/Mac
# For Windows, uncomment: venv\Scripts\activate
echo ""

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --upgrade pip setuptools wheel
echo ""

# Install requirements
echo "✓ Installing requirements..."
pip install -r requirements.txt
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "✓ Creating .env file..."
    cp .env.example .env
    echo "  .env file created - please update with your settings"
else
    echo "✓ .env file already exists"
fi
echo ""

# Create logs directory
echo "✓ Creating logs directory..."
mkdir -p logs
echo ""

# Run migrations
echo "✓ Running database migrations..."
python manage.py migrate
echo ""

# Create superuser
echo "✓ Creating superuser account..."
echo "  Please enter superuser credentials:"
python manage.py createsuperuser
echo ""

# Collect static files
echo "✓ Collecting static files..."
python manage.py collectstatic --noinput
echo ""

echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Review and update .env file settings"
echo "2. Run: python manage.py runserver"
echo "3. Access: http://localhost:8000"
echo "4. Admin: http://localhost:8000/admin"
echo ""
echo "For more information, see README.md"
