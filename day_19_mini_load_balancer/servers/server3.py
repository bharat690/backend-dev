from fastapi import FastAPI

#run on port 8003

app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hellow From Server 3"}

@app.get("/health")
def healthy():
    return True 