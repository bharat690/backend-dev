from sqlmodel import SQLModel, Field

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item_name: str = Field(min_length=5)
    mrp: int = Field(ge=0)
    cost_price: int = Field(ge=0)
    stock: int = Field(ge=0)