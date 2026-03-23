from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category',
                    'status', 'price', 'created_at')
    list_filter = ('status', 'category', 'instructor', 'created_at')
    search_fields = ('title', 'code', 'description')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('instructor',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('course', 'order')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'status', 'grade')
    list_filter = ('status', 'enrollment_date', 'grade')
    search_fields = ('student__username', 'course__title')
    raw_id_fields = ('student', 'course')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'created_at')
    search_fields = ('student__username', 'course__title')
    raw_id_fields = ('student', 'course')
