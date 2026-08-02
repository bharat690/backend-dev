from fastapi import FastAPI 
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from database.database import engine
from database.session import get_session 
from models.models import Item
from routes import item

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(item.app , tags=["Items"])
    

    
@app.get("/")
def home():
    return {
        "message": "Connected to Server"
    }
    
