from fastapi import APIRouter , Path , HTTPException

app = APIRouter()

@app.get("/transactions")
def get_transactions():
    pass


@app.post("/transactions")
def create_transaction():
    pass