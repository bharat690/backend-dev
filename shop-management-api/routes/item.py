from fastapi import APIRouter
from datetime import date
from validators.item import ItemRequest
from database.session import get_session
from models.models import Item 

app = APIRouter() ; 

@app.post("/items")
def addItem(item:ItemRequest):
    session = get_session()
    
    db_item = Item(
        item_name=item.item_name , 
        mrp=item.mrp ,
        cost_price=item.cost_price ,
        stock= item.stock,
        created_at=date.today()
    )
    
    session.add(db_item)
    session.commit()
    session.refresh(db_item)

    return db_item