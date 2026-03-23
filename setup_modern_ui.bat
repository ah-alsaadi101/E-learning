@echo off
REM EduLearn Modern UI Setup Script (Windows)
REM This script helps you implement the modern UI components

echo 🎨 EduLearn Modern UI Setup
echo =============================

REM Check if we're in the right directory
if not exist "manage.py" (
    echo ❌ Error: Please run this script from your Django project root directory
    pause
    exit /b 1
)

echo ✅ Django project detected

REM Check if static directory exists
if not exist "static" (
    echo 📁 Creating static directory...
    mkdir static\css
    mkdir static\js
    mkdir static\img
    echo ✅ Static directories created
) else (
    echo ✅ Static directory already exists
)

REM Check if modern templates exist
if exist "templates\base.html" (
    echo ⚠️  Base template already exists. Modern templates created as *_modern.html
    echo    You can manually replace the content or update your views to use the modern versions
) else (
    echo 📄 Base template not found. Modern templates created for reference
)

echo.
echo 🚀 Setup Complete!
echo.
echo Next steps:
echo 1. Review the modern templates in the templates/ directory
echo 2. Update your Django views to use the modern templates
echo 3. Run 'python manage.py collectstatic' to collect static files
echo 4. Start your development server and test the new UI
echo.
echo 📖 Read MODERN_UI_README.md for detailed implementation guide
echo.
echo 🎉 Happy coding!

pause