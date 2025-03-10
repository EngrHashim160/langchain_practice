from pydantic import BaseModel

class Student(BaseModel):
    name: str

new_student = {'name': 'Hashim'}

student = Student(**new_student)

print("Type: ", type(student))
print(student)