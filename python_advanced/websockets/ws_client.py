#!/usr/bin/env python3
import asyncio
import websockets


async def main():
    async with websockets.connect("ws://127.0.0.1:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(f"{response}")


asyncio.run(main())