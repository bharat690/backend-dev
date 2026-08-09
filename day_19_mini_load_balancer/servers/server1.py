from fastapi import FastAPI

#run on port 8001

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hellow From Server 1"}

@app.get("/health")
def healthy():
    return True 