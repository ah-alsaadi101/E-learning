from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source='student.username', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'student', 'student_name', 'course', 'course_title', 'amount',
                  'payment_method', 'payment_date', 'transaction_id', 'status']
        read_only_fields = ['id', 'payment_date']

    def validate(self, data):
        # Prevent duplicate payments for same student-course
        if Payment.objects.filter(
            student=data['student'],
            course=data['course'],
            status='completed'
        ).exists():
            raise serializers.ValidationError(
                "Payment already exists for this course")
        return data
