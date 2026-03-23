from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User
from courses.models import Category, Course, Enrollment


class CoursesAPITests(APITestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(
            username='instructor1',
            email='instructor@example.com',
            password='StrongPass123!',
            role='instructor',
        )
        self.student = User.objects.create_user(
            username='student1',
            email='student@example.com',
            password='StrongPass123!',
            role='student',
        )
        self.category = Category.objects.create(name='Programming')

    def test_instructor_can_create_course_without_sending_instructor_field(self):
        self.client.force_authenticate(user=self.instructor)
        response = self.client.post(
            '/api/courses/courses/',
            {
                'title': 'API Course',
                'description': 'Created from tests',
                'category': self.category.id,
                'price': '0.00',
                'status': 'published',
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['instructor'], self.instructor.id)
        self.assertTrue(Course.objects.filter(title='API Course', instructor=self.instructor).exists())

    def test_student_cannot_create_course(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.post(
            '/api/courses/courses/',
            {
                'title': 'Blocked Course',
                'description': 'Students should not create this',
                'category': self.category.id,
                'price': '0.00',
                'status': 'published',
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_student_can_enroll_in_free_course(self):
        course = Course.objects.create(
            title='Free Course',
            description='Free to enroll',
            category=self.category,
            instructor=self.instructor,
            price='0.00',
            status='published',
        )

        self.client.force_authenticate(user=self.student)
        response = self.client.post(
            '/api/courses/enrollments/',
            {
                'course': course.id,
            },
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Enrollment.objects.filter(student=self.student, course=course).exists()
        )
