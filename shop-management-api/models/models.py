from sqlmodel import SQLModel, Field
from datetime import date 
from typing import Literal


class Item(SQLModel, table=True):
    item_id: int | None = Field(
        default=None,
        primary_key=True
    )
    item_name: str = Field(min_length=5) # "Diet Coke -330mL"
    mrp: int = Field(ge=0) 
    cost_price: int = Field(ge=0)
    stock: int = Field(ge=0)
    created_at : date
    updated_at: date | None = None
    is_active: bool = Field(default=True)
    
class Batch(SQLModel , table = True):
    batch_id : int | None = Field(
        default=None,
        primary_key=True
    )
    item_id : int = Field(foreign_key="item.item_id")
    purchase_date : date = Field(default_factory=date.today) 
    expiry_date : date = Field(gt= date.today())
    purchased_qty : int = Field(ge=1) 
    remaining_qty : int = Field(gt=0)
    
class TransactionItem(SQLModel , table = True) : 
    transaction_item_id : int | None = Field(
        default=None,
        primary_key=True
    )
    transaction_id : int = Field(foreign_key="transaction.transaction_id")
    item_id : int = Field(foreign_key="item.item_id") 
    qty : int = Field(gt= 0 )

class Transaction(SQLModel , table=True):
    transaction_id: int | None = Field(
        default=None,
        primary_key=True
    )
    transaction_type: str = Field(default="Sale")
    payment_method: str = Field(default="Cash")
    amount : int = Field(ge=1)
    created_at: date = Field(default_factory=date.today)
    remark : str |None = Field(default=None)
        