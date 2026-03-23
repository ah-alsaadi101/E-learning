import os
import sys
import django
import argparse
from pathlib import Path
from random import choice, randint

# Initialize Django environment
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

from django.contrib.auth.hashers import make_password
from faker import Faker
from factory.django import DjangoModelFactory
from factory import SubFactory, LazyAttribute, Iterator
from accounts.models import User
from courses.models import Category, Course
from quizzes.models import Quiz, MCQuestion, Choice
from payments.models import Payment
from core.models import NewsAndEvents
from discussions.models import Post, Comment


fake = Faker()

# Factories


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = LazyAttribute(lambda x: fake.unique.user_name())
    email = LazyAttribute(lambda x: fake.unique.email())
    password = LazyAttribute(lambda x: make_password('password123'))
    first_name = LazyAttribute(lambda x: fake.first_name())
    last_name = LazyAttribute(lambda x: fake.last_name())
    phone = LazyAttribute(lambda x: fake.phone_number())
    address = LazyAttribute(lambda x: fake.address())
    role = Iterator(['student', 'instructor'])


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = LazyAttribute(lambda x: fake.unique.word().title())
    description = LazyAttribute(lambda x: fake.text(max_nb_chars=100))


class CourseFactory(DjangoModelFactory):
    class Meta:
        model = Course

    title = LazyAttribute(lambda x: fake.sentence(nb_words=5))
    slug = LazyAttribute(lambda x: fake.unique.slug())
    code = LazyAttribute(lambda x: fake.unique.bothify(text='??###').upper())
    description = LazyAttribute(lambda x: fake.paragraph(nb_sentences=4))
    category = SubFactory(CategoryFactory)
    instructor = SubFactory(UserFactory, role='instructor')
    price = LazyAttribute(lambda x: fake.pydecimal(
        left_digits=3, right_digits=2, positive=True))
    status = Iterator(['draft', 'published', 'archived'])


class QuizFactory(DjangoModelFactory):
    class Meta:
        model = Quiz

    course = SubFactory(CourseFactory)
    title = LazyAttribute(lambda x: fake.sentence(nb_words=4))
    slug = LazyAttribute(lambda x: fake.unique.slug())
    description = LazyAttribute(lambda x: fake.paragraph(nb_sentences=2))
    pass_mark = LazyAttribute(lambda x: randint(40, 90))
    random_order = LazyAttribute(lambda x: fake.boolean())
    answers_at_end = LazyAttribute(lambda x: fake.boolean())
    exam_paper = LazyAttribute(lambda x: fake.boolean())
    single_attempt = LazyAttribute(lambda x: fake.boolean())
    draft = LazyAttribute(lambda x: fake.boolean())


class MCQuestionFactory(DjangoModelFactory):
    class Meta:
        model = MCQuestion

    content = LazyAttribute(lambda x: fake.sentence(nb_words=12))
    explanation = LazyAttribute(lambda x: fake.sentence(nb_words=10))
    choice_order = Iterator(['content', 'random', 'none'])


class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    question = SubFactory(MCQuestionFactory)
    choice = LazyAttribute(lambda x: fake.sentence(nb_words=6))
    correct = False


class NewsAndEventsFactory(DjangoModelFactory):
    class Meta:
        model = NewsAndEvents

    title = LazyAttribute(lambda x: fake.sentence(nb_words=6))
    summary = LazyAttribute(lambda x: fake.paragraph(nb_sentences=2))
    content = LazyAttribute(lambda x: fake.paragraph(nb_sentences=4))
    post_type = Iterator(['news', 'event'])
    posted_as = Iterator(['news', 'event'])


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    course = SubFactory(CourseFactory)
    author = SubFactory(UserFactory, role='student')
    title = LazyAttribute(lambda x: fake.sentence(nb_words=6))
    content = LazyAttribute(lambda x: fake.paragraph(nb_sentences=3))


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    post = SubFactory(PostFactory)
    author = SubFactory(UserFactory, role='student')
    content = LazyAttribute(lambda x: fake.paragraph(nb_sentences=2))


def create_admin_user():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            first_name='Admin',
            last_name='User',
            role='admin'
        )
        print(' Created admin user')


def clear_data():
    Comment.objects.all().delete()
    Post.objects.all().delete()
    NewsAndEvents.objects.all().delete()
    Payment.objects.all().delete()
    Choice.objects.all().delete()
    MCQuestion.objects.all().delete()
    Quiz.objects.all().delete()
    Course.objects.all().delete()
    Category.objects.all().delete()
    User.objects.exclude(username='admin').delete()
    print(' Data cleared')


def generate_data(users=20, instructors=5, courses=10, quizzes=5, payments=15, news=8, posts=12, clear=False):
    if clear:
        clear_data()

    create_admin_user()

    instructors_list = UserFactory.create_batch(instructors, role='instructor')
    students_list = UserFactory.create_batch(users, role='student')

    categories = CategoryFactory.create_batch(max(2, courses // 2))
    course_objs = []
    for _ in range(courses):
        course = CourseFactory(category=choice(
            categories), instructor=choice(instructors_list))
        course_objs.append(course)

    quiz_objs = []
    for _ in range(quizzes):
        quiz = QuizFactory(course=choice(course_objs))
        quiz_objs.append(quiz)

    for quiz in quiz_objs:
        num_questions = randint(5, 10)
        for _ in range(num_questions):
            question = MCQuestionFactory()
            question.quiz.add(quiz)
            choice_objs = []
            for j in range(4):
                choice_obj = ChoiceFactory(question=question)
                choice_objs.append(choice_obj)
            if not any(c.correct for c in choice_objs):
                selected = choice(choice_objs)
                selected.correct = True
                selected.save()

    for _ in range(payments):
        Payment.objects.create(
            student=choice(students_list),
            course=choice(course_objs),
            amount=round(fake.pydecimal(
                left_digits=3, right_digits=2, positive=True), 2),
            payment_method=choice(['card', 'paypal', 'bank_transfer', 'cash']),
            status=choice(['completed', 'pending', 'failed'])
        )

    NewsAndEventsFactory.create_batch(news)

    posts_created = []
    for _ in range(posts):
        post = PostFactory(course=choice(course_objs),
                           author=choice(students_list))
        posts_created.append(post)

    for post in posts_created:
        for _ in range(randint(0, 5)):
            CommentFactory(post=post, author=choice(students_list))

    print(' Data generation completed')
    print(f'Users: {User.objects.count()}')
    print(f'Courses: {Course.objects.count()}')
    print(f'Quizzes: {Quiz.objects.count()}')
    print(f'Questions: {MCQuestion.objects.count()}')
    print(f'Choices: {Choice.objects.count()}')
    print(f'Payments: {Payment.objects.count()}')
    print(f'News/Events: {NewsAndEvents.objects.count()}')
    print(f'Posts: {Post.objects.count()}')
    print(f'Comments: {Comment.objects.count()}')


def main():
    parser = argparse.ArgumentParser(
        description='Seed EduLearn database with fake data')
    parser.add_argument('--users', type=int, default=20)
    parser.add_argument('--instructors', type=int, default=5)
    parser.add_argument('--courses', type=int, default=10)
    parser.add_argument('--quizzes', type=int, default=5)
    parser.add_argument('--payments', type=int, default=15)
    parser.add_argument('--news', type=int, default=8)
    parser.add_argument('--posts', type=int, default=12)
    parser.add_argument('--clear', action='store_true')
    args = parser.parse_args()

    generate_data(
        users=args.users,
        instructors=args.instructors,
        courses=args.courses,
        quizzes=args.quizzes,
        payments=args.payments,
        news=args.news,
        posts=args.posts,
        clear=args.clear,
    )


if __name__ == '__main__':
    main()
