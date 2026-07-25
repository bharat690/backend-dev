from fastapi import HTTPException 
from utils.basic_helpers import load_books , save_books


def add_new_book(data : dict)  :
    books = load_books() 
    
    for book in books:
        if book["isbn"] == data["isbn"]:
            raise HTTPException(
                status_code=400,
                detail="ISBN already exists"
            )

    books.append(data)
    save_books(books) 

    return {
        "message" : "Added New Book" 
    }

def get_book_by_id(id) :
    books = load_books() 

    for book in  books : 
        if(book["id"] == id) : 
            return book 

    raise HTTPException(status_code=404 , detail="ID doesnt Exists")


def get_all_books():
    data = load_books() 
    return {
        "Book Count" : len(data) ,
        "data" : data 
    }


