
from django.core.management import execute_from_command_line
from django.db import migrations
from django.contrib import admin
from celery import shared_task
from faker import Faker
import pytest
from course.models import Course, Program
import requests
from accounts.models import User
from django.core.management.base import BaseCommand
import csv
    help = 'Seed database with initial data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=10)
        parser.add_argument('--courses', type=int, default=5)

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Create users
        for i in range(options['users']):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role=fake.random_element(['student', 'instructor'])
            )

        # Create programs and courses
        for i in range(options['courses']):
            program = Program.objects.create(
                title=fake.sentence(nb_words=3),
                summary=fake.paragraph()
            )

            Course.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                instructor=User.objects.filter(role='instructor').first(),
                program=program,
                price=fake.random_int(50, 500)
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database')
        )
```

3. ** Run the command**:
```bash
python manage.py seed_data - -users 20 - -courses 10
```

# Method 4: CSV Import

# Creating CSV Import Command

```python


class Command(BaseCommand):
    help = 'Import users from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                User.objects.create_user(
                    username=row['username'],
                    email=row['email'],
                    password=row['password'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
        self.stdout.write('CSV import completed')


```

# Sample CSV Format (`users.csv`):
```csv
username, email, password, first_name, last_name
john_doe, john@example.com, password123, John, Doe
jane_smith, jane@example.com, password123, Jane, Smith
```

# Method 5: API-Based Data Entry

# Using Django REST Framework

If you have DRF set up, you can create data via API:

```python

# Create a course via API
data = {
    "title": "Python Programming",
    "description": "Learn Python from basics to advanced",
    "price": 99.99,
    "instructor": 1
}

headers = {'Authorization': 'Bearer your-token'}
response = requests.post(
    'http://localhost:8000/api/courses/', json=data, headers=headers)
```

# Bulk API Operations

```python
# Bulk create users
users_data = [
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"},
]

for user_data in users_data:
    response = requests.post(
        'http://localhost:8000/api/users/', json=user_data)
```

# Method 6: Database Direct Insertion

# Using Django Shell

```bash
python manage.py shell
```

```python

# Create users
for i in range(10):
    User.objects.create_user(
        username=f'user{i}',
        email=f'user{i}@example.com',
        password='password123'
    )

# Create programs and courses
program = Program.objects.create(title="Web Development")
Course.objects.create(
    title="Django Basics",
    description="Learn Django framework",
    program=program,
    price=49.99
)
```

# Method 7: Automated Testing Fixtures

# Using pytest-django fixtures

```python
# conftest.py

fake = Faker()


@pytest.fixture
def sample_user(db):
    return User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='password123'
    )


@pytest.fixture
def sample_course(db, sample_user):
    from course.models import Course, Program
    program = Program.objects.create(title="Test Program")
    return Course.objects.create(
        title="Test Course",
        description="Test description",
        instructor=sample_user,
        program=program
    )


```

# Method 8: Scheduled Data Generation

# Using Celery for Periodic Data Creation

```python
# tasks.py

fake = Faker()


@shared_task
def generate_sample_users(count=10):
    for _ in range(count):
        User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
    return f"Created {count} users"


```

# Method 9: Admin Bulk Actions

# Custom Admin Actions

```python
# admin.py


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions = ['generate_fake_users']

    def generate_fake_users(self, request, queryset):
        from faker import Faker
        fake = Faker()

        for _ in range(10):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
        self.message_user(request, "10 fake users created")
    generate_fake_users.short_description = "Generate 10 fake users"


```

# Method 10: Data Migration

# Using Django Migrations

```python
# migrations/0002_seed_initial_data.py


def seed_data(apps, schema_editor):
    User = apps.get_model('accounts', 'User')
    fake = Faker()

    for _ in range(5):
        User.objects.create(
            username=fake.user_name(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]


```

# Quick Start Commands

# For Development Data
```bash
# Run existing factory scripts
cd scripts
python generate_fake_accounts_data.py
python generate_fake_core_data.py
python generate_fake_data.py

# Or create a custom seed command
python manage.py seed_data - -users 50 - -courses 20
```

# For Production Data
```bash
# Load fixtures
python manage.py loaddata initial_data.json

# Or use management commands
python manage.py import_csv users.csv
```

# Best Practices

1. ** Use Transactions**: Wrap bulk operations in database transactions
2. ** Validate Data**: Always validate data before saving
3. ** Handle Duplicates**: Check for existing records to avoid duplicates
4. ** Performance**: Use bulk_create() for large datasets
5. ** Security**: Never hardcode passwords in production
6. ** Environment**: Use different data for development vs production
7. ** Backup**: Always backup before running bulk operations

# Troubleshooting

# Common Issues

1. ** IntegrityError**: Foreign key constraints - ensure related objects exist first
2. ** ValidationError**: Model validation - check field requirements
3. ** DuplicateKeyError**: Unique constraints - check for existing records
4. ** MemoryError**: Large datasets - process in batches

# Debugging Tips

```python
# Check existing data
User.objects.all().count()
Course.objects.all().count()

# Clear data if needed
User.objects.all().delete()
Course.objects.all().delete()

# Reset sequences (PostgreSQL)
execute_from_command_line(
    ['manage.py', 'sqlsequencereset', 'accounts', 'course'])
``` < /content >
<parameter name = "filePath" > E: \django\merged_elearning\AUTOMATIC_DATA_ENTRY_GUIDE.md
