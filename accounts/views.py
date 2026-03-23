from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm


@login_required
def profile(request):
    enrollments = request.user.enrollments.select_related('course').all()
    created_courses = request.user.courses.select_related('category').all()
    return render(request, 'accounts/profile.html', {
        'profile_user': request.user,
        'enrollments': enrollments,
        'created_courses': created_courses,
        'payments_count': request.user.payments.count(),
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 'Account created successfully! Please log in.')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
