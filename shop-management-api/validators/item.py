from pydantic import BaseModel , Field

class ItemRequest(BaseModel):
    item_name : str = Field(min_length=4 , max_length= 20)
    mrp : int = Field(description="in paise" , ge = 100 )
    cost_price :int = Field(description="in paise" , ge = 20)
    stock : int = Field(ge=0)
    
class ItemResponse(BaseModel):
    item_id : int 
    item_name : str 
    mrp : int
    cost_price : int 
    stock : int
