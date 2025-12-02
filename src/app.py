"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path
from sqlalchemy.orm import Session
from db import SessionLocal, init_db, seed_db, Activity, Student

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# NOTE: activities are now persisted in the DB.


@app.on_event("startup")
def on_startup():
    # Ensure DB tables exist and seed initial activities
    init_db()
    db = SessionLocal()
    try:
        seed_db(db)
    finally:
        db.close()


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities(db: Session = Depends(get_db)):
    db_activities = db.query(Activity).all()
    result = {}
    for a in db_activities:
        result[a.name] = {
            "description": a.description,
            "schedule": a.schedule,
            "max_participants": a.max_participants,
            "participants": [s.email for s in a.participants],
        }
    return result


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str, db: Session = Depends(get_db)):
    """Sign up a student for an activity"""
    # Validate activity exists
    activity = db.query(Activity).filter(Activity.name == activity_name).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Validate student is not already signed up
    if any(p.email == email for p in activity.participants):
        raise HTTPException(
            status_code=400,
            detail="Student is already signed up"
        )
    # get or create student
    student = db.query(Student).filter(Student.email == email).first()
    if not student:
        student = Student(email=email)
        db.add(student)
        db.commit()
        db.refresh(student)

    # enforce capacity if provided
    if activity.max_participants is not None and len(activity.participants) >= activity.max_participants:
        raise HTTPException(status_code=400, detail="Activity is full")

    activity.participants.append(student)
    db.add(activity)
    db.commit()
    return {"message": f"Signed up {email} for {activity_name}"}


@app.delete("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str, db: Session = Depends(get_db)):
    """Unregister a student from an activity"""
    # Validate activity exists
    activity = db.query(Activity).filter(Activity.name == activity_name).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Validate student is signed up
    student = db.query(Student).filter(Student.email == email).first()
    if not student or student not in activity.participants:
        raise HTTPException(
            status_code=400,
            detail="Student is not signed up for this activity"
        )
    activity.participants.remove(student)
    db.add(activity)
    db.commit()
    return {"message": f"Unregistered {email} from {activity_name}"}

