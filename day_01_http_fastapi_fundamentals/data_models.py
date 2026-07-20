from pydantic import BaseModel , EmailStr 
from typing import Literal

class Student(BaseModel):
    name : str  
    email : EmailStr 
    age : int 
    course : Literal["Cloud Computing","Data Science", "AI/ML","Cyber Security", "Software Engineering"]
    isActive : bool 

