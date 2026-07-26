from fastapi import FastAPI , Path 

from validators.model import BookCreate , MemberCreate , BookResponse , MemberResponse , MembersResponse

from utils.member import get_all_member , get_member_by_id , register_member
from utils.basic_helpers import load_ids , save_ids 
from utils.book import get_all_books , get_book_by_id ,add_new_book 
from utils.library_mechanism import return_book , borrow_books



app = FastAPI()



@app.get("/")
def home():
    return {
        "message":"connected successfully"
    }

@app.get("/members" , response_model= MembersResponse )
def getMembers():
    return get_all_member()

@app.get("/members/{id}",response_model=MemberResponse)
def getMembersByID(id : int = Path(... )):
    return get_member_by_id(id)
    

@app.post("/members")
def registerMember(data : MemberCreate):

    data = data.model_dump()

    id_cred = load_ids() 
    id_cred[0]["member_id"] = id_cred[0]["member_id"] + 1
    id = id_cred[0]["member_id"] 

    save_ids(id_cred)
    
    data["id"] = id 

    return register_member(data)

@app.post("/books")
def addBook(book : BookCreate):
    data = book.model_dump()
    
    id_cred = load_ids() 
    id_cred[0]["book_id"] = id_cred[0]["book_id"] + 1
    id = id_cred[0]["book_id"] 
    
    save_ids(id_cred)
        
    data["id"] = id 
    
    return add_new_book(data)

@app.get("/books/{id}")
def getBookByID(id : int = Path(...)):
    return get_book_by_id(id) 

@app.get("/books" , response_model=BookResponse)
def getBooks():
    return get_all_books()

@app.post("/members/{id}/borrow/{book_id}")
def borrowBook(id : int = Path(...) , 
               book_id : int = Path(...)):
    return borrow_books( id , book_id )
    

@app.post("/borrow-records/{borrow_id}/return")
def returnBook(borrow_id : int = Path(...)):
    return return_book(borrow_id)