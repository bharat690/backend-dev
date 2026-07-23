from fastapi import FastAPI , Path 
from model import  Book , Borrow_Book , Member
from member import get_all_member , get_member_by_id , register_member

app = FastAPI()

id = 10000 
book_id = 10000 


@app.get("/")
def home():
    return {
        "message":"connected successfully"
    }

@app.get("/members")
def getMembers():
    return get_all_member()

@app.get("/members/{id}")
def getMembersByID(id : int = Path(... )):
    return get_member_by_id(id)
    

@app.post("/members")
def registerMember(data : Member):

    global id 
    data = data.model_dump()
    id = id + 1 
    data["id"] = id 

    return register_member(data)

@app.post("/books")
def addBook():
    pass

@app.get("/books/{id}")
def getBookByID():
    pass

@app.get("/books")
def getBooks():
    pass

@app.post("/members/{id}/borrow/{book_id}")
def borrowBook():
    pass

@app.post("/borrow-records/{borrow_id}/return")
def returnBook():
    pass