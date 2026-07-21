from fastapi import FastAPI , HTTPException , Path , Query
from typing import Literal
from model import BookModel

app = FastAPI()

lastID = 10000 
books = []


@app.get("/")
def home():
    return {
        "message":"Connected !"
    }


@app.get("/book/{id}")
def getBookbyID(id : int = Path(gt = 10000)):
    for book in books : 
        if(book.get("id") == id) : 
            return{
                "data":book ,
                "message":"Data Retrieved Successfully" 
            }
        

    raise HTTPException(status_code=404 , detail="No Data for Such Id")


@app.get("/books")
def get_books(
    category: Literal[
        "Fiction",
        "Non-Fiction",
        "Science",
        "History",
        "Biography"
    ] | None = Query(
        None,
        description="Select a book category."
    ) , 

    author: str | None = Query(None, description="Filter by Author"),
    min_price: int = Query(0, description="Minimum Price Filter"),
    max_price: int = Query(99999, description="Max Price Filter"),
    in_stock: bool = Query(False, description="To Retrieve only available books."),
    page_no: int = Query(0, description="Pagination.")
):
    data = books
    if category:
        data = [book for book in data if book.get("category") == category]
    if author:
        data = [book for book in data if book.get("author") == author]
    data = [
        book for book in data
        if min_price <= book.get("price", 0) <= max_price
    ]
    if in_stock:
        data = [book for book in data if book.get("stock", 0)]
    if page_no > 0:
        per_page = 10
        start = (page_no - 1) * per_page
        end = start + per_page
        data = data[start:end]
    return {
        "data": data,
        "count": len(data)
    }

    


@app.post("/books")
def createBook(data : BookModel):
    global lastID 

    data = data.model_dump()
    for book in books : 
        if(book["isbn"] == data["isbn"]):
            raise HTTPException(status_code=400 , detail="Duplicate ISBN")
    data["id"] = lastID + 1 ; 
    lastID = lastID + 1 ; 
    books.append(data) ; 

    return { 
        "message":"Data Pushed Successfully"
    }

@app.put("/book/{id}")
def updateBook(
    update_val : BookModel ,
    id : int = Path(...) 
               ):
    
    update_val = update_val.model_dump()
    found = False ; 
    for book in books : 
        if(book["id"] == id and book["isbn"] == update_val["isbn"]): 
            found = True 
            book.update(update_val)
        if(book["id"] == id and book["isbn"] != update_val["isbn"]):
            for existing_book in books : 
                if(existing_book["isbn"] == update_val["isbn"]):
                    raise HTTPException(status_code = 400 , detail="Duplicate ISBN")
            book.update(update_val)
            found = True

    if(found) : 
        return{
            "message":"Values Updated Successfully"
        }
    else :
        raise HTTPException(status_code=404 , detail="ID not Found.")
    

@app.delete("/book/{id}")
def deleteBook(id : int = Path):
    for book in books : 
        if(id == book.get("id")):
            books.pop(books.index(book))
            return {
                "message":"Removed data Successfully"
            }
        
    raise HTTPException(status_code=404 , detail="ID doesnt exists")