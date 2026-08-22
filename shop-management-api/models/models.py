from sqlmodel import SQLModel, Field
from datetime import date, datetime
from typing import Optional


class User(SQLModel, table=True):
    """
    User model for authentication
    """
    __tablename__ = "users"
    
    user_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    username: str = Field(
        unique=True,
        index=True,
        min_length=3,
        max_length=50
    )
    email: str = Field(
        unique=True,
        index=True,
        max_length=100
    )
    hashed_password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)


class Item(SQLModel, table=True):
    """
    Item model - represents products in inventory
    """
    __tablename__ = "items"
    
    item_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    item_name: str = Field(
        min_length=2,
        max_length=100,
        index=True
    )
    mrp: int = Field(ge=0, description="Maximum Retail Price in paise")
    cost_price: int = Field(ge=0, description="Cost Price in paise")
    stock: int = Field(ge=0, default=0)
    created_at: date = Field(default_factory=date.today)
    updated_at: Optional[date] = Field(default=None)
    is_active: bool = Field(default=True)


class Batch(SQLModel, table=True):
    """
    Batch model - tracks purchase batches for items
    Used for FIFO and expiry tracking
    """
    __tablename__ = "batches"
    
    batch_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    item_id: int = Field(foreign_key="items.item_id", index=True)
    purchase_date: date = Field(default_factory=date.today)
    expiry_date: Optional[date] = Field(default=None)
    purchased_qty: int = Field(ge=1)
    remaining_qty: int = Field(ge=0)
    cost_price_per_unit: int = Field(ge=0, description="Cost price at time of purchase")
    is_active: bool = Field(default=True)


class Transaction(SQLModel, table=True):
    """
    Transaction model - records sales and purchases
    """
    __tablename__ = "transactions"
    
    transaction_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    transaction_type: str = Field(description="Sale, Purchase, Return, etc.")
    payment_method: str = Field(default="Cash")
    amount: int = Field(ge=0, description="Total amount in paise")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    remark: Optional[str] = Field(default=None, max_length=500)
    created_by: Optional[int] = Field(
        default=None,
        foreign_key="users.user_id"
    )


class TransactionItem(SQLModel, table=True):
    """
    TransactionItem model - junction table for transactions and items
    """
    __tablename__ = "transaction_items"
    
    transaction_item_id: Optional[int] = Field(
        default=None,
        primary_key=True
    )
    transaction_id: int = Field(foreign_key="transactions.transaction_id", index=True)
    item_id: int = Field(foreign_key="items.item_id", index=True)
    batch_id: Optional[int] = Field(
        default=None,
        foreign_key="batches.batch_id"
    )
    qty: int = Field(ge=1)
    unit_price: int = Field(ge=0, description="Price per unit at time of transaction")
    cost_price: int = Field(ge=0, description="Cost price for profit calculation")