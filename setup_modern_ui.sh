#!/bin/bash

# EduLearn Modern UI Setup Script
# This script helps you implement the modern UI components

echo "🎨 EduLearn Modern UI Setup"
echo "============================"

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from your Django project root directory"
    exit 1
fi

echo "✅ Django project detected"

# Check if static directory exists
if [ ! -d "static" ]; then
    echo "📁 Creating static directory..."
    mkdir -p static/css
    mkdir -p static/js
    mkdir -p static/img
    echo "✅ Static directories created"
else
    echo "✅ Static directory already exists"
fi

# Check if modern templates exist
if [ -f "templates/base.html" ]; then
    echo "⚠️  Base template already exists. Modern templates created as *_modern.html"
    echo "   You can manually replace the content or update your views to use the modern versions"
else
    echo "📄 Base template not found. Modern templates created for reference"
fi

echo ""
echo "🚀 Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Review the modern templates in the templates/ directory"
echo "2. Update your Django views to use the modern templates"
echo "3. Run 'python manage.py collectstatic' to collect static files"
echo "4. Start your development server and test the new UI"
echo ""
echo "📖 Read MODERN_UI_README.md for detailed implementation guide"
echo ""
echo "🎉 Happy coding!"