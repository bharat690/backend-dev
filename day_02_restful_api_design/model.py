from pydantic import BaseModel , Field
from typing import Literal

class BookModel(BaseModel):
    title : str
    author : str 
    stock : int
    isbn : str
    price : int = Field(gt=0 , lt=99999)
    category : Literal['Fiction', 'Non-Fiction', 'Science', 'History', 'Biography'] 
    pub_year : int = Field(gt=1400)