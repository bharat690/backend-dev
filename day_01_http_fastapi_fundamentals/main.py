from fastapi import FastAPI , HTTPException ,Query , Path
from data_models import Student
from pydantic import PositiveInt

app  = FastAPI()

global lastId 
lastId = 0 


container = []

@app.get("/")
def home() : 
    return {"message":"Connected to Server"}

@app.get("/Student")
def getStudent(
    id : PositiveInt = Query(description="Search by ID , 0 to get all " , default=0 ,  )
):
    if(id == 0 & lastId != 0 ) : 
        return container
    
    for ele in container : 
        if  ele.get("id") == id :
            return ele
    
    return {
        "message" : "No Student Exists",
    }


@app.post("/Student")
def registerStudent(data : Student):

    global lastId 


    data = data.model_dump()
    lastId = lastId +  1
    data["id"] = lastId  
    container.append(data)

    return {
        "message":"Data added Successfully"
    }


@app.put("/Student")
def updateStudent():
    pass

