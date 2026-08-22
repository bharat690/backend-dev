import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///inventory.db")

engine = create_engine(
    DATABASE_URL,
    echo=False,  # S
    pool_pre_ping=True,  
    pool_size=10,
    max_overflow=20
)