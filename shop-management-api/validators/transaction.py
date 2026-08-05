from pydantic import BaseModel , Field
from typing import Literal
from datetime import date

class TransactionResponse():
    transaction_id : int 
    transaction_type : str
    payment_method : str
    amount : int 
    created_at: date 
    remark : str | None 
    
class TransactionRequest():
    transaction_type : str
    payment_method : Literal["Cash" , "Cheque" , "UPI" , "Bank Transfer"]
    amount : int = Field(ge=1)
    created_at: date = Field(default_factory=date.today)
    remark : str | None = Field(default = None)