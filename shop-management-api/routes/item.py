from fastapi import APIRouter , Path , HTTPException
from datetime import date
from sqlmodel import select
from validators.item import ItemRequest, ItemResponse
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

@app.get("/items", response_model= list[ItemResponse])
def getItems():
    statement = select(Item)
    session = get_session()
    result = session.exec(statement)
    
    items = result.all()
    
    return items

@app.get("/items/{id}", response_model= ItemResponse)
def getItemById(id :int = Path(description="enter id")):
    statement = select(Item).where(Item.item_id == id)
    
    session = get_session()
    
    result=session.exec(statement)
    
    item = result.first()
    
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )


    
    return item
    
    
    
    