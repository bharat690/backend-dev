from fastapi import FastAPI 
from db.database import connect_db

app = FastAPI()

@app.get("/")
def home():

    conn = connect_db()

    cur = conn.cursor()

    cur.execute("SELECT version();")

    version = cur.fetchone()

    cur.close()
    conn.close()

    return {
        "database": version[0]
    }