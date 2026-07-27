import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def connect_db():
    try:
        conn = psycopg.connect(DATABASE_URL)
        print("Connected Successfully")
        return conn
    except Exception as e:
        print(e)
        return None