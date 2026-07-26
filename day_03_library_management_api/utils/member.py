from pathlib import Path
from fastapi import HTTPException
from typing import List , Dict 
from utils.basic_helpers import load_members , save_members




def get_all_member():
    data = load_members() 
    return {
        "Members_Count" : len(data) ,
        "data" : data 
    }

def get_member_by_id(id : int):
    data = load_members()

    for member in data : 
        if(member["id"] == id) :
            return member
        
    raise HTTPException(status_code=404 , detail="ID doesnt Exists")

def register_member(member : Dict):
    data = load_members()

    for iter in data :
        if member["email"] == iter["email"] :
            raise HTTPException(status_code=400 , detail="Duplicate Email")
        
    data.append(member) 

    save_members(data)

    return {
        "message" : "Member Registered Successfully"
    } 

    


    

