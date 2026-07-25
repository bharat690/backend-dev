from pathlib import Path 
from typing import List , Dict
from fastapi import HTTPException
from utils.member import   load_members
from utils.basic_helpers import (
    load_members,
    load_books,
    save_books,
    load_json,
    save_json,
    load_ids,
    save_ids
)
import json
from datetime import date 


def count_books(dataset , member_id) -> int :
    counter = 0 
    for item in dataset : 
         if(item["member_id"] == member_id and item["status"] == "BORROWED"):
              counter = counter + 1 

    return counter

def borrow_books(id, book_id):

    members = load_members()
    books = load_books()

    member_exists = False
    for member in members:
        if member["id"] == id:
            member_exists = True
            membership = member["membership"]
            break

    if not member_exists:
        raise HTTPException(status_code=404, detail="Member doesn't exist")

    book_exists = False
    for book in books:
        if book["id"] == book_id:
            book_exists = True
            stock = book["stock"]
            break

    if not book_exists:
        raise HTTPException(status_code=404, detail="Book doesn't exist")

    if stock <= 0:
        raise HTTPException(status_code=409, detail="Out of stock")

    borrow_path = Path("data/borrow_records.json")
    Borrow_Data = load_json(borrow_path)
    bookHolded = count_books(Borrow_Data, id)

    for record in Borrow_Data:
        if (
            record["book_id"] == book_id
            and record["status"] == "BORROWED"
        ):
            raise HTTPException(status_code=409, detail="Book already borrowed")

    if membership == "Free" and bookHolded >= 3:
        raise HTTPException(status_code=400, detail="Upgrade Membership")

    if membership == "Elite" and bookHolded >= 5:
        raise HTTPException(status_code=400, detail="Upgrade Membership")

    if membership == "Master" and bookHolded >= 10:
        raise HTTPException(status_code=400, detail="Max Book Limit Reached")

    for book in books:
        if book["id"] == book_id:
            book["stock"] -= 1
            break

    save_books(books)

    ids_cred = load_ids()
    ids_cred[0]["borrow_id"] += 1
    save_ids(ids_cred)

    borrow_id = ids_cred[0]["borrow_id"]

    Borrow_Data.append({
        "borrow_id": borrow_id,
        "book_id": book_id,
        "member_id": id,
        "status": "BORROWED",
        "borrow_date": date.today().isoformat()
    })

    save_json(Borrow_Data, borrow_path)

    return {
        "message": "Book assigned"
    }
    
def return_book(borrow_id):
    borrow_path = Path("data/borrow_records.json")
    Borrow_Data = load_json(borrow_path)

    record_found = False

    for record in Borrow_Data:
        if record["borrow_id"] == borrow_id:

            if record["status"] == "RETURNED":
                raise HTTPException(
                    status_code=400,
                    detail="Book already returned"
                )

            record_found = True
            book_id = record["book_id"]
            record["status"] = "RETURNED"
            break

    if not record_found:
        raise HTTPException(
            status_code=404,
            detail="Borrow ID doesn't exist"
        )

    books = load_books()

    for book in books:
        if book["id"] == book_id:
            book["stock"] += 1
            break

    save_books(books)
    save_json(Borrow_Data, borrow_path)

    return {
        "message": "Book returned successfully"
    }
    

        
