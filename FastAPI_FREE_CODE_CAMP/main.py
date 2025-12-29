from fastapi import FastAPI, Path
from typing import Optional


app = FastAPI()


students = {
    1: {"name": "Alice", "age": 20, "subject": "Physics"},
    2: {"name": "Bob", "age": 22, "subject": "Mathematics"},
    3: {"name": "Charlie", "age": 23, "subject": "Chemistry"},
}

@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.get("/students")
def list_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student to retrieve", gt=0, lt=100)):
    return students.get(student_id, {"error": "Student not found"})


# @app.get("/get-by-subject")
# def get_students_by_subject(subject: Optional[str] = None):
# # def get_students_by_subject(*, subject: Optional[str] = None, test: int): #We can not use anything after Optional so we use *,
#     if subject is None:
#         return {"error": "Subject query parameter is required"}
#     result = {id: info for id, info in students.items() if info["subject"].lower() == subject.lower()}
#     return result if result else {"error": "No students found for the given subject"}


@app.get("/get-by-subject/{student_id}")
def get_students_by_subject(student_id: int, subject: Optional[str] = None):
# def get_students_by_subject(*, subject: Optional[str] = None, test: int): #We can not use anything after Optional so we use *,
    if subject is None:
        return {"error": "Subject query parameter is required"}
    result = {id: info for id, info in students.items() if info["subject"].lower() == subject.lower()}
    return result if result else {"error": "No students found for the given subject"}
    