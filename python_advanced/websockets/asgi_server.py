#!/usr/bin/env python3
import uvicorn
from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Mount, Route, WebSocketRoute
from starlette.websockets import WebSocket, WebSocketDisconnect
from starlette.staticfiles import StaticFiles

HOST = "127.0.0.1"
PORT = 8000

CLIENTS = set()


async def homepage(request):
    """Serve the homepage."""
    return FileResponse("static/index.html")


async def ws_endpoint(websocket: WebSocket):
    """Handle a single WebSocket client."""
    await websocket.accept()
    print(f"Client connected: {websocket.client}")
    CLIENTS.add(websocket)
    try:
        while True:
            message = await websocket.receive_text()
            if not message.strip():
                continue
            print(f"Received: {message}")
            await broadcast(message)
    except WebSocketDisconnect:
        pass
    finally:
        CLIENTS.discard(websocket)
        print(f"Client disconnected: {websocket.client}")


async def broadcast(message):
    """Send a message to every connected client."""
    for client in list(CLIENTS):
        try:
            await client.send_text(message)
        except Exception:
            CLIENTS.discard(client)


routes = [
    Route("/", homepage),
    WebSocketRoute("/ws", ws_endpoint),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

app = Starlette(routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
