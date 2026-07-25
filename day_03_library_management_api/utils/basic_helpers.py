import json
from typing import List , Dict 
from pathlib import Path





def load_json(DATA_FILE) -> List[Dict]:
    with open(DATA_FILE , 'r' , encoding="utf-8") as file : 
        return json.load(file) 


def save_json(data , DATA_FILE):
    with open(DATA_FILE , 'w' , encoding="utf-8") as file : 
            json.dump(data , file , indent= 4 , ensure_ascii= False)
            
ID_PATH = Path("data/id_counter.json")

def load_ids():
    return load_json(ID_PATH)

def save_ids(ids):
    save_json(ids , ID_PATH)
    
MEMBER_DATA_FILE = Path("data/member.json")

def load_members():
    return load_json(MEMBER_DATA_FILE) 

def save_members(data):
    save_json(data , MEMBER_DATA_FILE)
    
    

BOOK_DATA_FILE = Path("data/book.json")

def load_books():
    return load_json(BOOK_DATA_FILE) 

def save_books(data):
    save_json(data , BOOK_DATA_FILE)