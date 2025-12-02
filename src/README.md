# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

The application now persists activities, students and signups using SQLite by default (configured in `DATABASE_URL`).
Database tables are automatically created and seeded on startup in development. In production, configure a proper DB URL (e.g. Postgres) and use Alembic for migrations.

### Running with SQLite (dev)

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run the app:

   ```
   uvicorn app:app --reload --port 8000
   ```

3. The app will create `dev.db` and seed initial activities on first run.
