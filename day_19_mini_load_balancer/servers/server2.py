from fastapi import FastAPI

#run on port 8002


app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hellow From Server 2"}

@app.get("/health")
def healthy():
    return True 