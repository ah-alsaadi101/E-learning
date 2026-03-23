from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'amount',
                    'payment_method', 'status', 'payment_date')
    list_filter = ('status', 'payment_method', 'payment_date')
    search_fields = ('student__username', 'course__title', 'transaction_id')
    readonly_fields = ('payment_date',)
    raw_id_fields = ('student', 'course')
