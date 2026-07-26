from pydantic import BaseModel , Field , EmailStr
from typing import Literal 
from datetime import date  



class BookCreate(BaseModel) :
    isbn : str 
    title : str
    author : str 
    stock : int = Field(ge = 0)
    
class BookResponse(BaseModel) : 
    id : int 
    isbn : str 
    title : str
    author : str 
    stock : int = Field(ge = 0)
    
class MemberCreate(BaseModel):
    name : str 
    membership : Literal["Free","Elite","Master"]
    email : EmailStr

class Borrow_Book(BaseModel) : 
    member_id : int 
    book_id : int 
    borrow_date : date = Field(default= date.today())
    status : Literal["BORROWED","RETURNED","LOST"]

class MemberResponse(BaseModel) : 
    id : int 
    name : str 
    membership : Literal["Free","Elite","Master"]
    email : EmailStr
    
    
class MembersResponse(BaseModel):
    Members_Count: int
    data: list[MemberResponse]