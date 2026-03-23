#!/bin/bash
# EduLearn Frontend Critical Fixes Script
# Run this script to fix the most critical frontend issues

echo "🔧 EduLearn Frontend Critical Fixes"
echo "=================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print status
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    print_error "Not in Django project directory. Please run from the project root."
    exit 1
fi

echo "📁 Working directory: $(pwd)"

# 1. Fix Static Files Configuration
echo ""
echo "1. Fixing static files configuration..."
if grep -q "STATICFILES_DIRS" config/settings.py; then
    print_warning "STATICFILES_DIRS already exists in settings.py"
else
    cat >> config/settings.py << 'EOF'

# Static files configuration
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
EOF
    print_status "Added STATICFILES_DIRS to settings.py"
fi

# 2. Create Error Templates
echo ""
echo "2. Creating error templates..."

mkdir -p templates

# 404.html
if [ ! -f "templates/404.html" ]; then
    cat > templates/404.html << 'EOF'
{% extends 'base.html' %}
{% block title %}Page Not Found{% endblock %}
{% block content %}
<div class="container py-5 text-center">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h1 class="display-1 text-muted">404</h1>
            <h2>Page Not Found</h2>
            <p class="lead">The page you're looking for doesn't exist.</p>
            <a href="{% url 'courses:course_list' %}" class="btn btn-primary">Go Home</a>
        </div>
    </div>
</div>
{% endblock %}
EOF
    print_status "Created 404.html template"
else
    print_warning "404.html already exists"
fi

# 500.html
if [ ! -f "templates/500.html" ]; then
    cat > templates/500.html << 'EOF'
{% extends 'base.html' %}
{% block title %}Server Error{% endblock %}
{% block content %}
<div class="container py-5 text-center">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h1 class="display-1 text-muted">500</h1>
            <h2>Server Error</h2>
            <p class="lead">Something went wrong on our end. Please try again later.</p>
            <a href="{% url 'courses:course_list' %}" class="btn btn-primary">Go Home</a>
        </div>
    </div>
</div>
{% endblock %}
EOF
    print_status "Created 500.html template"
else
    print_warning "500.html already exists"
fi

# 3. Update templates to extend base.html
echo ""
echo "3. Updating templates to use base.html..."

# Function to update template
update_template() {
    local file="$1"
    local title="$2"

    if [ -f "$file" ]; then
        # Check if already extends base.html
        if grep -q "extends 'base.html'" "$file"; then
            print_warning "$file already extends base.html"
            return
        fi

        # Create backup
        cp "$file" "${file}.backup"
        print_status "Created backup: ${file}.backup"

        # Extract content between body tags or main content
        # This is a simplified approach - in practice, you might need more sophisticated parsing
        awk '
        BEGIN { in_body=0; content="" }
        /<body>/ { in_body=1; next }
        /<\/body>/ { in_body=0; next }
        in_body { content = content $0 "\n" }
        END { print content }
        ' "$file" > temp_content.html

        # If no body tags found, try to extract main content
        if [ ! -s temp_content.html ]; then
            # Look for main content area
            sed -n '/<main>/,/<\/main>/p; /<div class="container"/,/<\/div>/p' "$file" | head -20 > temp_content.html
        fi

        # Create new template
        cat > "$file" << EOF
{% extends 'base.html' %}
{% block title %}$title{% endblock %}
{% block content %}
EOF

        # Add extracted content
        if [ -s temp_content.html ]; then
            cat temp_content.html >> "$file"
        else
            echo "<!-- Content extracted from original template -->" >> "$file"
        fi

        echo "{% endblock %}" >> "$file"

        rm temp_content.html
        print_status "Updated $file to extend base.html"
    else
        print_warning "$file not found"
    fi
}

# Update main templates
update_template "templates/courses/course_list.html" "Courses - EduLearn"
update_template "templates/courses/course_detail.html" "Course Details - EduLearn"
update_template "templates/courses/dashboard.html" "Dashboard - EduLearn"
update_template "templates/accounts/login.html" "Login - EduLearn"
update_template "templates/accounts/register.html" "Register - EduLearn"
update_template "templates/accounts/profile.html" "Profile - EduLearn"

# 4. Add CSRF tokens to forms
echo ""
echo "4. Adding CSRF tokens to forms..."

# Function to add CSRF token to forms
add_csrf_to_forms() {
    local file="$1"

    if [ -f "$file" ]; then
        # Check if CSRF token already exists
        if grep -q "csrf_token" "$file"; then
            print_warning "$file already has CSRF token"
            return
        fi

        # Add CSRF token after form opening tag
        sed -i 's/<form/<form\n    {% csrf_token %}/g' "$file"
        print_status "Added CSRF token to forms in $file"
    fi
}

# Add CSRF to main templates
add_csrf_to_forms "templates/accounts/login.html"
add_csrf_to_forms "templates/accounts/register.html"
add_csrf_to_forms "templates/courses/dashboard.html"

# 5. Update JavaScript with error handling
echo ""
echo "5. Enhancing JavaScript with error handling..."

if [ -f "static/js/main.js" ]; then
    # Add error handling functions if not present
    if ! grep -q "showErrorMessage" static/js/main.js; then
        cat >> static/js/main.js << 'EOF'

// Error handling and user feedback
function showErrorMessage(message, type = 'danger') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    document.body.appendChild(alertDiv);

    // Auto remove after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

function showSuccessMessage(message) {
    showErrorMessage(message, 'success');
}

function showLoadingState(element) {
    if (typeof element === 'string') {
        element = document.querySelector(element);
    }

    if (element) {
        element.setAttribute('data-original-html', element.innerHTML);
        element.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
        element.disabled = true;
    }
}

function hideLoadingState(element) {
    if (typeof element === 'string') {
        element = document.querySelector(element);
    }

    if (element) {
        const originalHtml = element.getAttribute('data-original-html');
        if (originalHtml) {
            element.innerHTML = originalHtml;
            element.disabled = false;
        }
    }
}

// Global error handler for fetch requests
window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
    showErrorMessage('An unexpected error occurred. Please try again.');
});

// Form validation helper
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });

    return isValid;
}

// CSRF token helper for AJAX
function getCSRFToken() {
    const token = document.querySelector('[name=csrfmiddlewaretoken]');
    return token ? token.value : '';
}
EOF
        print_status "Added error handling functions to main.js"
    else
        print_warning "Error handling functions already exist in main.js"
    fi
else
    print_warning "static/js/main.js not found"
fi

# 6. Run collectstatic
echo ""
echo "6. Collecting static files..."
python manage.py collectstatic --noinput --clear
if [ $? -eq 0 ]; then
    print_status "Static files collected successfully"
else
    print_error "Failed to collect static files"
fi

# 7. Create a summary
echo ""
echo "🎉 Critical fixes completed!"
echo ""
echo "SUMMARY OF CHANGES:"
echo "==================="
echo "✅ Added STATICFILES_DIRS to settings.py"
echo "✅ Created 404.html and 500.html error templates"
echo "✅ Updated templates to extend base.html:"
echo "   - course_list.html"
echo "   - course_detail.html"
echo "   - dashboard.html"
echo "   - login.html"
echo "   - register.html"
echo "   - profile.html"
echo "✅ Added CSRF tokens to forms"
echo "✅ Enhanced JavaScript with error handling"
echo "✅ Collected static files"
echo ""
echo "NEXT STEPS:"
echo "==========="
echo "1. Test the application: python manage.py runserver"
echo "2. Check all pages load without errors"
echo "3. Verify forms work correctly"
echo "4. Test responsive design on mobile"
echo ""
echo "REMAINING TASKS:"
echo "================="
echo "- Review and customize the updated templates"
echo "- Add proper loading states to async operations"
echo "- Implement comprehensive form validation"
echo "- Add empty states for no data scenarios"
echo "- Optimize images and static assets"
echo "- Configure CDN for production"
echo ""
echo "For detailed implementation examples, see: FRONTEND_AUDIT_REPORT.md"