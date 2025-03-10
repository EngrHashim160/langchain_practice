from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # basic example
    # name: str 

    # default value
    name: str = 'hashim'

    # optional field
    age: Optional[int] = None

    # coerce

    # builtin validation i.e Emailstr
    email: EmailStr

    # Field Function-> Default values, constraints, description and regrex expressions
    cgpa: float = Field(gt=0, lt= 4, default=1.0,
                        description="A decimal Value representing the cgpa of the student")

    




# new_student = {'name': 'Hashim'}

# new_student = {'name': 123} # it will give error

# default values
# new_student = {}

# optional fields
# new_student = {} # age=None
# new_student = {"age": 23}

# coerce
# new_student = {
#     "age": "23"     # still it will understand and type coerce it to int
# }


# built-in Validation i.e EmailStr
# new_student = {
#     "age": '23',
#     # "email": 'abc' # error not a valid value of email
#     "email": 'abc@gmail.com' # now okay
# }

# Field Function
new_student = {
    "age": '23',
    # "email": 'abc' # error not a valid value of email
    "email": 'abc@gmail.com', # now okay
    # "cgpa":5 # error: input field should be less than 4
    # "cgpa": 3.5 # now okay
    # default... cgpa: 1.0
}


 # returns pydantic object -> convert to json/dict - do it...
student = Student(**new_student)

print("Type: ", type(student))
print(student)