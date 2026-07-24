from pathlib import Path 
from typing import List , Dict
from fastapi import HTTPException
from utils.member import   load_members
from utils.book import save_books ,  load_books
import json
from datetime import date 



def load_json(DATA_FILE) -> List[Dict]:
    with open(DATA_FILE , 'r' , encoding="utf-8") as file : 
        return json.load(file) 


def save_json(data , DATA_FILE):
    with open(DATA_FILE , 'w' , encoding="utf-8") as file : 
            json.dump(data , file , indent= 4 , ensure_ascii= False)

ID_PATH = Path("data/id_counter.json")

def load_ids():
    return load_json(ID_PATH)

def save_ids(ids):
    save_json(ids , ID_PATH)

def count_books(dataset , member_id) -> int :
    counter = 0 
    for item in dataset : 
         if(item["member_id"] == member_id and item["status"] == "BORROWED"):
              counter = counter + 1 

    return counter

def borrow_books(id , book_id) : 

    
    members = load_members()
    books = load_books() 

    member_exists = False
    for member in members :
        if member["id"] == id  : 
            member_exists = True 
            membership = member["membership"]


    if not member_exists : 
         raise HTTPException(status_code=300 , detail="member doesnt exists")

    book_exists = False
    for book in books :
        if book["id"] == book_id  : 
            book_exists = True 
            stock = book["stock"] 
            book["stock"] = book["stock"] - 1 
            
            
    if not book_exists :
         raise HTTPException(status_code=300 , detail="book doesnt exists")
    if not stock : 
         raise HTTPException(status_code=503 , detail="out of stock")
     
    
    
    borrow_path = Path("data/borrow_records.json")
    Borrow_Data = load_json(borrow_path)
    bookHolded = count_books(Borrow_Data , id)
    if(membership == "Free" and bookHolded == 3 ) :
        raise HTTPException(status_code=400 , detail="Upgarde Membership" )
    if(membership == "Elite" and bookHolded == 5 ) :
            raise HTTPException(status_code=400 , detail="Upgarde Membership" )
    if(membership == "Master" and bookHolded == 10 ) :
            raise HTTPException(status_code=400 , detail="Max Book Limit Reached" )
        
    save_books(books)


    
    ids_cred = load_ids()
    ids_cred[0]["borrow_id"]  = ids_cred[0]["borrow_id"]  + 1 

    save_ids(ids_cred)
    borrow_id = ids_cred[0]["borrow_id"] 
    
    Borrow_Data.append(
    {
        "borrow_id" : borrow_id , 
        "book_id" : book_id ,
        "member_id" : id , 
        "status":"BORROWED" , 
        "borrow_date" : date.today().isoformat()
    }
    )

    save_json(Borrow_Data , borrow_path)
    
    return{
        "message" : "book assigned"
    }
        
    
def return_book(borrow_id):
    borrow_path = Path("data/borrow_records.json")
    Borrow_Data = load_json(borrow_path)
    
    
    
    record_found = False 
    for record in Borrow_Data : 
        if record["borrow_id"] == borrow_id : 
            if record["status"] == "RETURNED":
                raise HTTPException(status_code=300 , detail="already returned")
            record_found = True 
            book_id = record["book_id"] 
            record["status"] = "RETURNED"
            
    if not record_found :
        raise HTTPException(status_code=300 , detail="borrow id doesnt exists")
        
    books = load_books()    
    for book in books : 
        if(book["id"] == book_id):
            book["stock"] = book["stock"] + 1 
            
    save_books(books) 
    save_json(Borrow_Data, borrow_path)
    
    return{
        "message" : "book returned successfully"
    }
    

        
