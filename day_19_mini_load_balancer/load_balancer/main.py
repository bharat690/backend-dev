from fastapi import FastAPI
import httpx

app = FastAPI()

currServer = 0

servers_addresses = [
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8002",
    "http://127.0.0.1:8003"
]


def is_healthy(server):
    try:
        response = httpx.get(
            server + "/health",
            timeout=2
        )

        return response.status_code == 200

    except (httpx.ConnectError, httpx.TimeoutException):
        return False


@app.get("/")
def load_balancer():

    global currServer

    total_servers = len(servers_addresses)

    for _ in range(total_servers):

        server = servers_addresses[currServer]

        currServer = (currServer + 1) % total_servers

        if is_healthy(server):

            response = httpx.get(server)

            return response.json()

    return {
        "error": "No healthy servers available"
    }