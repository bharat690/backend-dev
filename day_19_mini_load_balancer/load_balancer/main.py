from fastapi import FastAPI
from fastapi.responses import RedirectResponse 
import httpx

app = FastAPI()
currServer = 0

@app.get("/")

def load_balancer():
    servers_addresses = ["http://127.0.0.1:8001" , "http://127.0.0.1:8002" , "http://127.0.0.1:8003"]
    
    global currServer
    
    if currServer == 2  :
        currServer = 0 
        server = 2
    else :
        currServer += 1 
        server = currServer - 1
    
    result = httpx.get(servers_addresses[server])  
    
    return result.json()
    
    
    
    