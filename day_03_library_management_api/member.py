import json
from pathlib import Path
from fastapi import HTTPException
from typing import List , Dict 

DATA_FILE = Path("member.json")

def load_members() -> List[Dict]:
    with open(DATA_FILE , 'r' , encoding="utf-8") as file : 
        return json.load(file) 


def save_members(data):
    with open(DATA_FILE , 'w' , encoding="utf-8") as file : 
            json.dump(data , file , indent= 4 , ensure_ascii= False)


def get_all_member():
    data = load_members() 
    return {
        "Members Count" : len(data) ,
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

    


    

