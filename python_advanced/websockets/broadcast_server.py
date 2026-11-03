#!/usr/bin/env python3
import asyncio
import websockets

HOST = "127.0.0.1"
PORT = 8765

CLIENTS = set()


async def handler(websocket):
    """Handle a single client connection."""
    print(f"Client connected: {websocket.remote_address}")
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            if not message.strip():
                await websocket.send(f"ERR:EMPTY")
            print(f"Received: {message}")
            websockets.broadcast(CLIENTS, f"{message}")
    except websockets.ConnectionClosed:
        pass
    finally:
        CLIENTS.discard(websocket)
        print(f"Client disconnected: {websocket.remote_address}")


async def main():
    async with websockets.serve(handler, HOST, PORT):
        await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")