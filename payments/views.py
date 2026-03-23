from uuid import uuid4

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum
from django.shortcuts import get_object_or_404, redirect, render

from courses.models import Course, Enrollment
from .models import Payment


@login_required
def payment_list(request):
    if request.user.role == 'admin':
        payments = Payment.objects.select_related('student', 'course')
    else:
        payments = Payment.objects.filter(
            student=request.user).select_related('course')
    successful_payments = payments.filter(status='completed')
    pending_payments = payments.filter(status='pending')
    aggregates = successful_payments.aggregate(
        total_spent=Sum('amount'),
        average_payment=Avg('amount'),
    )
    return render(request, 'payments/payment_list.html', {
        'payments': payments,
        'successful_payments': successful_payments,
        'pending_payments': pending_payments,
        'total_spent': aggregates['total_spent'] or 0,
        'average_payment': aggregates['average_payment'] or 0,
    })


@login_required
def create_payment(request, course_id):
    course = get_object_or_404(Course, id=course_id, status='published')
    if request.method != 'POST':
        return redirect('courses:course_detail', slug=course.slug)

    if request.user.role != 'student':
        messages.error(request, 'Only students can make course payments.')
        return redirect('courses:course_detail', slug=course.slug)

    if course.price <= 0:
        messages.info(request, 'This course is free, so no payment is required.')
        Enrollment.objects.get_or_create(student=request.user, course=course)
        return redirect('courses:course_detail', slug=course.slug)

    payment, created = Payment.objects.get_or_create(
        student=request.user,
        course=course,
        defaults={
            'amount': course.price,
            'payment_method': 'card',
            'transaction_id': f"AUTO-{uuid4().hex[:10].upper()}",
            'status': 'completed',
        },
    )
    if not created and payment.status != 'completed':
        payment.amount = course.price
        payment.payment_method = 'card'
        payment.transaction_id = f"AUTO-{uuid4().hex[:10].upper()}"
        payment.status = 'completed'
        payment.save()

    Enrollment.objects.get_or_create(student=request.user, course=course)
    messages.success(request, f'Payment recorded for {course.title}.')
    return redirect('courses:course_detail', slug=course.slug)


@login_required
def payment_detail(request, payment_id):
    payment = get_object_or_404(
        Payment.objects.select_related('student', 'course', 'course__instructor'),
        id=payment_id,
    )
    if request.user.role != 'admin' and payment.student != request.user:
        messages.error(request, 'You do not have permission to view that payment.')
        return redirect('payments:payment_list')

    return render(request, 'payments/payment_detail.html', {'payment': payment})
