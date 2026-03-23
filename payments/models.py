from django.db import models
from django.conf import settings


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, default='card')
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), (
        'completed', 'Completed'), ('failed', 'Failed')], default='completed')

    def __str__(self):
        return f"{self.student.username} - {self.course.title} - ${self.amount}"

    class Meta:
        unique_together = ['student', 'course']  # Prevent duplicate payments
        ordering = ['-payment_date']
