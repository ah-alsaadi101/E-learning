from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Payment


@login_required
def payment_list(request):
    if request.user.role == 'admin':
        payments = Payment.objects.select_related('student', 'course')
    else:
        payments = Payment.objects.filter(
            student=request.user).select_related('course')
    return render(request, 'payments/payment_list.html', {'payments': payments})
