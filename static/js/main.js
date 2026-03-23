/**
 * Custom JavaScript for EduLearn E-Learning Platform
 */

// Global variables
let currentTheme = 'light';

// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeTheme();
    initializeTooltips();
    initializeAlerts();
    initializeFormValidation();
    initializeLoadingStates();
    initializeAnimations();
});

// Theme Management
function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
}

function setTheme(theme) {
    currentTheme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);

    // Update theme toggle button if exists
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.innerHTML = theme === 'light'
            ? '<i class="bi bi-moon-stars"></i>'
            : '<i class="bi bi-sun"></i>';
    }
}

function toggleTheme() {
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
}

// Tooltip Initialization
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Alert Management
function initializeAlerts() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        if (!alert.classList.contains('alert-permanent')) {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        }
    });
}

// Form Validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                showLoadingState(form);
            }
            form.classList.add('was-validated');
        }, false);
    });
}

// Loading States
function initializeLoadingStates() {
    // Add loading state to buttons with data-loading attribute
    const loadingButtons = document.querySelectorAll('[data-loading]');
    loadingButtons.forEach(button => {
        button.addEventListener('click', function() {
            showLoadingState(this);
        });
    });
}

function showLoadingState(element) {
    const originalText = element.innerHTML;
    const loadingText = element.getAttribute('data-loading') || 'Loading...';

    element.innerHTML = `
        <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
        ${loadingText}
    `;
    element.disabled = true;

    // Store original text for restoration
    element.setAttribute('data-original-text', originalText);

    // Auto-restore after 10 seconds (fallback)
    setTimeout(() => {
        hideLoadingState(element);
    }, 10000);
}

function hideLoadingState(element) {
    const originalText = element.getAttribute('data-original-text');
    if (originalText) {
        element.innerHTML = originalText;
        element.disabled = false;
        element.removeAttribute('data-original-text');
    }
}

// Animation Utilities
function initializeAnimations() {
    // Add intersection observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe elements with animation classes
    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

// Utility Functions
function showAlert(message, type = 'info', duration = 5000) {
    const alertContainer = document.getElementById('alert-container') ||
                          createAlertContainer();

    const alertId = 'alert-' + Date.now();
    const alertHTML = `
        <div id="${alertId}" class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;

    alertContainer.insertAdjacentHTML('beforeend', alertHTML);

    // Auto-dismiss
    if (duration > 0) {
        setTimeout(() => {
            const alert = document.getElementById(alertId);
            if (alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, duration);
    }
}

function createAlertContainer() {
    const container = document.createElement('div');
    container.id = 'alert-container';
    container.className = 'position-fixed top-0 end-0 p-3';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
    return container;
}

// Course Card Interactions
function initializeCourseCards() {
    const courseCards = document.querySelectorAll('.course-card');

    courseCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('card-hover');
        });

        card.addEventListener('mouseleave', function() {
            this.classList.remove('card-hover');
        });
    });
}

// Quiz Functionality
function initializeQuiz() {
    const quizOptions = document.querySelectorAll('.quiz-option');

    quizOptions.forEach(option => {
        option.addEventListener('click', function() {
            // Remove selected class from all options
            quizOptions.forEach(opt => opt.classList.remove('selected'));
            // Add selected class to clicked option
            this.classList.add('selected');

            // Store selected answer
            const questionId = this.closest('.quiz-question').dataset.questionId;
            const answerId = this.dataset.answerId;
            storeQuizAnswer(questionId, answerId);
        });
    });
}

function storeQuizAnswer(questionId, answerId) {
    const answers = JSON.parse(localStorage.getItem('quiz_answers') || '{}');
    answers[questionId] = answerId;
    localStorage.setItem('quiz_answers', JSON.stringify(answers));
}

// Search Functionality
function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    if (searchInput && searchResults) {
        let searchTimeout;

        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            const query = this.value.trim();

            if (query.length < 2) {
                searchResults.innerHTML = '';
                return;
            }

            searchTimeout = setTimeout(() => {
                performSearch(query);
            }, 300);
        });
    }
}

async function performSearch(query) {
    try {
        const response = await fetch(`/search/?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        displaySearchResults(data.results);
    } catch (error) {
        console.error('Search error:', error);
        showAlert('Search failed. Please try again.', 'danger');
    }
}

function displaySearchResults(results) {
    const searchResults = document.getElementById('search-results');

    if (results.length === 0) {
        searchResults.innerHTML = '<p class="text-muted">No results found.</p>';
        return;
    }

    const resultsHTML = results.map(result => `
        <div class="search-result-item mb-3 p-3 border rounded">
            <h6 class="mb-1">
                <a href="${result.url}" class="text-decoration-none">${result.title}</a>
            </h6>
            <p class="text-muted small mb-0">${result.description}</p>
        </div>
    `).join('');

    searchResults.innerHTML = resultsHTML;
}

// Dashboard Charts (if Chart.js is included)
function initializeCharts() {
    if (typeof Chart !== 'undefined') {
        // Progress Chart
        const progressCtx = document.getElementById('progress-chart');
        if (progressCtx) {
            new Chart(progressCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Completed', 'In Progress', 'Not Started'],
                    datasets: [{
                        data: [65, 25, 10],
                        backgroundColor: ['#10b981', '#f59e0b', '#e5e7eb'],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        }
    }
}

// Keyboard Shortcuts
document.addEventListener('keydown', function(event) {
    // Ctrl/Cmd + K: Focus search
    if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
        event.preventDefault();
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.focus();
        }
    }

    // Escape: Close modals
    if (event.key === 'Escape') {
        const modals = document.querySelectorAll('.modal.show');
        modals.forEach(modal => {
            const bsModal = bootstrap.Modal.getInstance(modal);
            if (bsModal) {
                bsModal.hide();
            }
        });
    }
});

// Performance Optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export functions for global use
window.EduLearn = {
    toggleTheme,
    showAlert,
    showLoadingState,
    hideLoadingState,
    debounce
};
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
