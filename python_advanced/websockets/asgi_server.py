#!/usr/bin/env python3
import uvicorn
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket, WebSocketDisconnect

HOST = "127.0.0.1"
PORT = 8000

CLIENTS = set()


async def homepage(request):
    """Serve the homepage."""
    return HTMLResponse("<h1>WebSocket Echo</h1>")


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
]

app = Starlette(routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
