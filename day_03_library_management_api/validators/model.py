from pydantic import BaseModel , Field , EmailStr
from typing import Literal 
from datetime import date  

class Book(BaseModel) :
    isbn : str 
    title : str
    author : str 
    stock : int = Field(ge = 0)

class Borrow_Book(BaseModel) : 
    member_id : int 
    book_id : int 
    borrow_date : date = Field(... , default= date.today() ,  le = date.today())
    status : Literal["BORROWED","RETURNED","LOST"]

class Member(BaseModel) : 
    name : str 
    membership : Literal["Free","Elite","Master"]
    email : EmailStr
