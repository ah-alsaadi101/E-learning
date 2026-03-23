from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())
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
        student = data.get('student') or getattr(
            self.instance, 'student', self.context['request'].user
        )
        course = data.get('course') or getattr(self.instance, 'course', None)
        if not course:
            return data

        queryset = Payment.objects.filter(
            student=student,
            course=course,
        )
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "A payment record already exists for this course")
        return data
