from pydantic import BaseModel , Field , EmailStr
from typing import Literal 
from datetime import date  

class Book(BaseModel) :
    isbn : str 
    title : str
    author : str 
    stock : int 

class Borrow_Book(BaseModel) : 
    member_id : int 
    book_id : int 
    borrow_date : date = Field(... , le = date.today())
    status : Literal["BORROWED","RETURNED","LOST"]

class Member(BaseModel) : 
    id : int 
    name : str 
    membership : Literal["Free","Elite","Master"]
    email : EmailStr
