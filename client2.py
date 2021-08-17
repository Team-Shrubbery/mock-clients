import socketio
from time import time, sleep
import random
import json


import asyncio

sio = socketio.AsyncClient(json=json)


@sio.event
async def connect():
    print("Player 2 Connected")
    await sio.emit("message", "Player 2")


@sio.event
async def message(data):
    print("Player2 Received Message:", data)
    await sio.emit("my response", "A listener that was triggered by response")


@sio.event
async def move(data):
    print("Player 2 Received Move: ", data)


@sio.event
async def disconnect():
    print("Player 2 Disconnected from server")


async def main():
    await sio.connect("http://localhost:8000")

    # await sio.wait()


if __name__ == "__main__":
    asyncio.run(main())
    while True:
        a_move = random.choice(["2LEFT", "2RIGHT", "2UP", "2DOWN"])
        sio.emit("move", a_move)
        sleep(2)

# while True:
#     a_move = random.choice(["2LEFT", "2RIGHT", "2UP", "2DOWN"])
#     sio.emit(
#         "move",
#         a_move,
#     )
#     sleep(2)

# sio.wait()
