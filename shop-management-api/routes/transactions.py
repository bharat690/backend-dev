from fastapi import APIRouter  , HTTPException , Query
from pydantic import PositiveInt
from database.session import get_session
from models.models import Transaction
from validators.transaction import TransactionRequest , TransactionResponse
from sqlmodel import select
from typing import List 



app = APIRouter()

@app.get("/transactions" ,  response_model= List[TransactionResponse])
def get_transactions(
    amountGreaterThan : PositiveInt = Query(description="Amount More Than Filter" , default=0) ,
    
    ):
    session = get_session()
    statement = select(Transaction)
    
    result = session.exec(statement)
    
    item = result.all()
    
    return item
    


@app.post("/transactions")
def create_transaction():
    pass