from django.db import models
from django.conf import settings
from django.utils.text import slugify


def _generate_unique_value(model_class, field_name, base_value, instance_pk=None, max_length=None):
    value = (base_value or '').strip() or field_name
    if max_length:
        value = value[:max_length]

    candidate = value
    counter = 2
    while model_class.objects.filter(**{field_name: candidate}).exclude(pk=instance_pk).exists():
        suffix = f"-{counter}"
        trimmed_value = value[:max_length - len(suffix)] if max_length else value
        candidate = f"{trimmed_value}{suffix}"
        counter += 1
    return candidate


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Course(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    code = models.CharField(max_length=20, unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='courses')
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = _generate_unique_value(
                Course,
                'slug',
                slugify(self.title) or 'course',
                instance_pk=self.pk,
                max_length=self._meta.get_field('slug').max_length,
            )
        if not self.code:
            self.code = _generate_unique_value(
                Course,
                'code',
                slugify(self.title).replace('-', '').upper()[:12] or 'COURSE',
                instance_pk=self.pk,
                max_length=self._meta.get_field('code').max_length,
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    video = models.FileField(
        upload_to='lessons/videos/', blank=True, null=True)
    image = models.ImageField(
        upload_to='lessons/images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ['order', 'created_at']


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    # Grades from first project
    assignment_score = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    mid_exam_score = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    quiz_score = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    attendance_score = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    final_exam_score = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    total_score = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True)
    grade_point = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('enrolled', 'Enrolled'), (
        'completed', 'Completed'), ('failed', 'Failed')], default='enrolled')

    def save(self, *args, **kwargs):
        # Calculate total and grade
        scores = [self.assignment_score, self.mid_exam_score,
                  self.quiz_score, self.attendance_score, self.final_exam_score]
        valid_scores = [s for s in scores if s is not None]
        if valid_scores:
            self.total_score = sum(valid_scores)
            self.grade = self.calculate_grade(self.total_score)
            self.grade_point = self.calculate_grade_point(self.grade)
        super().save(*args, **kwargs)

    def calculate_grade(self, total):
        if total >= 90:
            return 'A+'
        elif total >= 85:
            return 'A'
        elif total >= 80:
            return 'A-'
        elif total >= 75:
            return 'B+'
        elif total >= 70:
            return 'B'
        elif total >= 65:
            return 'B-'
        elif total >= 60:
            return 'C+'
        elif total >= 55:
            return 'C'
        elif total >= 50:
            return 'C-'
        elif total >= 45:
            return 'D'
        else:
            return 'F'

    def calculate_grade_point(self, grade):
        points = {'A+': 4.0, 'A': 4.0, 'A-': 3.75, 'B+': 3.5, 'B': 3.0, 'B-': 2.75,
                  'C+': 2.5, 'C': 2.0, 'C-': 1.75, 'D': 1.0, 'F': 0.0}
        return points.get(grade, 0.0)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

    @property
    def progress(self):
        return 100 if self.status == 'completed' else 0

    @property
    def completed_lessons(self):
        lessons = self.course.lessons.all()
        return lessons if self.status == 'completed' else lessons.none()

    @property
    def time_spent(self):
        return '0h'

    class Meta:
        unique_together = ['student', 'course']
        ordering = ['-enrollment_date']


class Favorite(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

    class Meta:
        unique_together = ['student', 'course']
        ordering = ['-created_at']
