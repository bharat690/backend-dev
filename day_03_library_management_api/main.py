from fastapi import FastAPI , Path 

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"connected successfully"
    }

@app.get("/members")
def passHelper():
    pass

@app.get("/members/{id}")
def passHelper():
    pass

@app.post("/members")
def passHelper():
    pass

@app.post("/books")
def passHelper():
    pass

@app.get("/books/{id}")
def passHelper():
    pass

@app.get("/books")
def passHelper():
    pass

@app.post("/members/{id}/borrow/{book_id}")
def passHelper():
    pass

@app.post("/borrow-records/{borrow_id}/return")
def passHelper():
    pass