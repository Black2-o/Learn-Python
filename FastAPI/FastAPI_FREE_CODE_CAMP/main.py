from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


students = {
    1: {"name": "Alice", "age": 20, "subject": "Physics"},
    2: {"name": "Bob", "age": 22, "subject": "Mathematics"},
    3: {"name": "Charlie", "age": 23, "subject": "Chemistry"},
}

class Student(BaseModel):
    name: str
    age: int
    subject: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    subject: Optional[str] = None


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
    

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student ID already exists"}
    students[student_id] = student.dict()
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student not found"}
    
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.subject is not None:
        students[student_id]["subject"] = student.subject
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted successfully"}