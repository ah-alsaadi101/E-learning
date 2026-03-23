# API Documentation

Complete documentation for all REST API endpoints in the E-Learning Platform.

## Authentication

### Get Token (Login)

**Endpoint:** `POST /api/accounts/users/login/`

**Request:**

```json
{
  "username": "john",
  "password": "securepass123"
}
```

**Response (200):**

```json
{
  "token": "abc123def456...",
  "user": {
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "role": "student",
    "first_name": "John",
    "last_name": "Doe"
  }
}
```

**Headers for subsequent requests:**

```
Authorization: Token abc123def456...
```

---

### Register New User

**Endpoint:** `POST /api/accounts/users/register/`

**Request:**

```json
{
  "username": "jane",
  "email": "jane@example.com",
  "password": "securepass123",
  "first_name": "Jane",
  "last_name": "Doe",
  "role": "student"
}
```

**Response (201):**

```json
{
  "token": "xyz789...",
  "user": {...}
}
```

**Valid roles:**

- `student` - Regular student
- `instructor` - Course instructor
- `admin` - System administrator

---

## Courses API

### List Courses

**Endpoint:** `GET /api/courses/courses/`

**Query Parameters:**

- `page` (int) - Page number (default: 1)
- `category` (int) - Filter by category ID
- `status` (string) - draft, published, archived
- `instructor` (int) - Filter by instructor ID

**Response:**

```json
{
  "count": 25,
  "next": "http://localhost:8000/api/courses/courses/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Python Basics",
      "slug": "python-basics",
      "code": "PYTHON101",
      "description": "Learn Python fundamentals",
      "category": 1,
      "category_name": "Programming",
      "instructor": 5,
      "instructor_name": "John Smith",
      "price": "99.99",
      "status": "published",
      "lessons_count": 15,
      "enrollments_count": 42,
      "created_at": "2024-03-20T10:30:00Z",
      "updated_at": "2024-03-20T10:30:00Z"
    }
  ]
}
```

---

### Get Course Detail

**Endpoint:** `GET /api/courses/courses/{id}/`

**Response:**

```json
{
  "id": 1,
  "title": "Python Basics",
  "description": "Learn Python fundamentals...",
  "category": 1,
  "instructor": 5,
  "price": "99.99",
  "status": "published",
  "image": "http://localhost:8000/media/courses/python.jpg",
  "lessons_count": 15,
  "enrollments_count": 42
}
```

---

### Create Course (Instructor Only)

**Endpoint:** `POST /api/courses/courses/`

**Request:**

```json
{
  "title": "Advanced Python",
  "description": "Master advanced Python concepts",
  "category": 1,
  "price": "199.99",
  "status": "draft"
}
```

**Response (201):** Created course object

---

## Lessons API

### List Lessons

**Endpoint:** `GET /api/courses/lessons/`

**Query Parameters:**

- `course` (int) - Filter by course ID (required)
- `page` (int) - Page number

**Response:**

```json
{
  "count": 15,
  "results": [
    {
      "id": 1,
      "course": 1,
      "course_title": "Python Basics",
      "title": "Introduction to Python",
      "content": "In this lesson...",
      "video": "http://localhost:8000/media/lessons/intro.mp4",
      "image": "http://localhost:8000/media/lessons/intro.jpg",
      "order": 1,
      "created_at": "2024-03-20T10:30:00Z"
    }
  ]
}
```

---

## Enrollments API

### Get User Enrollments

**Endpoint:** `GET /api/courses/enrollments/`

**Response:**

```json
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "student": 10,
      "course": 1,
      "course_title": "Python Basics",
      "enrollment_date": "2024-03-20T10:30:00Z",
      "status": "enrolled",
      "grade": "A",
      "total_score": 95.5
    }
  ]
}
```

---

### Enroll in Course

**Endpoint:** `POST /api/courses/enrollments/`

**Request:**

```json
{
  "course": 1
}
```

**Response (201):** Enrollment object

---

## Quizzes API

### List Quizzes

**Endpoint:** `GET /api/quizzes/quizzes/`

**Query Parameters:**

- `course` (int) - Filter by course
- `category` (string) - assignment, exam, practice
- `draft` (boolean) - Include draft quizzes

**Response:**

```json
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "course": 1,
      "course_title": "Python Basics",
      "title": "Module 1 Quiz",
      "description": "Test your knowledge...",
      "category": "practice",
      "pass_mark": 70,
      "questions_count": 10,
      "draft": false,
      "created_at": "2024-03-20T10:30:00Z"
    }
  ]
}
```

---

### Start Quiz Attempt

**Endpoint:** `POST /api/quizzes/quizzes/{id}/start_attempt/`

**Response (201):**

```json
{
  "id": 1,
  "student": 10,
  "quiz": 1,
  "current_score": 0,
  "percent_correct": 0,
  "start": "2024-03-20T15:30:00Z",
  "completed": false
}
```

---

### Submit Quiz Answer

**Endpoint:** `POST /api/quizzes/attempts/{id}/submit_answer/`

**Request:**

```json
{
  "question_id": "123",
  "answer": "option_a"
}
```

**Response:**

```json
{
  "message": "Answer submitted successfully"
}
```

---

### Complete Quiz Attempt

**Endpoint:** `POST /api/quizzes/attempts/{id}/complete_attempt/`

**Response:**

```json
{
  "id": 1,
  "student": 10,
  "quiz": 1,
  "current_score": 70,
  "percent_correct": 85.5,
  "start": "2024-03-20T15:30:00Z",
  "end": "2024-03-20T15:45:00Z",
  "completed": true
}
```

---

## Discussions API

### List Posts

**Endpoint:** `GET /api/discussions/posts/`

**Query Parameters:**

- `course` (int) - Filter by course
- `author` (int) - Filter by author
- `page` (int) - Page number

**Response:**

```json
{
  "count": 25,
  "results": [
    {
      "id": 1,
      "course": 1,
      "course_title": "Python Basics",
      "author": 10,
      "author_name": "john",
      "title": "How to debug in Python?",
      "content": "Can anyone explain...",
      "comments_count": 5,
      "created_at": "2024-03-20T10:30:00Z"
    }
  ]
}
```

---

### Create Post

**Endpoint:** `POST /api/discussions/posts/`

**Request:**

```json
{
  "course": 1,
  "title": "How to debug?",
  "content": "Can anyone help me understand..."
}
```

**Response (201):** Created post object

---

### Add Comment to Post

**Endpoint:** `POST /api/discussions/posts/{id}/add_comment/`

**Request:**

```json
{
  "content": "You can use the pdb module..."
}
```

**Response (201):**

```json
{
  "id": 1,
  "author": 10,
  "author_name": "john",
  "content": "You can use the pdb module...",
  "created_at": "2024-03-20T15:30:00Z"
}
```

---

## Payments API

### List Payments

**Endpoint:** `GET /api/payments/payments/`

**Query Parameters:**

- `status` (string) - pending, completed, failed
- `page` (int) - Page number

**Response:**

```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "student": 10,
      "student_name": "john",
      "course": 1,
      "course_title": "Python Basics",
      "amount": "99.99",
      "payment_method": "card",
      "payment_date": "2024-03-20T10:30:00Z",
      "status": "completed"
    }
  ]
}
```

---

### Create Payment

**Endpoint:** `POST /api/payments/payments/`

**Request:**

```json
{
  "course": 1,
  "amount": "99.99",
  "payment_method": "card"
}
```

**Response (201):** Created payment object

---

## News & Events API

### List News

**Endpoint:** `GET /api/core/news-events/`

**Query Parameters:**

- `type` (string) - news, event
- `page` (int) - Page number

**Response:**

```json
{
  "count": 15,
  "results": [
    {
      "id": 1,
      "title": "New Course Available",
      "summary": "We've launched a new course...",
      "content": "Full content here...",
      "post_type": "news",
      "posted_as": "news",
      "created_at": "2024-03-20T10:30:00Z"
    }
  ]
}
```

---

## Error Responses

### 400 Bad Request

```json
{
  "error": "Field 'username' is required"
}
```

### 401 Unauthorized

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found

```json
{
  "detail": "Not found."
}
```

### 500 Server Error

```json
{
  "detail": "Internal server error"
}
```

---

## Filtering Examples

```bash
# Get published courses only
GET /api/courses/courses/?status=published

# Get courses from category 1
GET /api/courses/courses/?category=1

# Get practice quizzes
GET /api/quizzes/quizzes/?category=practice

# Get posts from a specific course
GET /api/discussions/posts/?course=1

# Get completed payments
GET /api/payments/payments/?status=completed
```

---

## Pagination Example

```bash
# Get page 2 with custom page size
GET /api/courses/courses/?page=2

# Response includes:
{
  "count": 100,
  "next": "http://localhost:8000/api/courses/courses/?page=3",
  "previous": "http://localhost:8000/api/courses/courses/?page=1",
  "results": [...]
}
```

---

## Rate Limiting

In production, rate limiting is configured as:

- 100 requests per hour per IP address
- 1000 requests per hour per authenticated user

---

## CORS Configuration

For frontend applications, configure CORS in `.env`:

```
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```
