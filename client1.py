import socketio
from time import time, sleep
import random
import json


import asyncio

sio = socketio.AsyncClient(json=json)


@sio.event
async def connect():
    print("Player 1 Connected")
    await sio.emit("message", "Player 1")


@sio.event
async def message(data):
    print("Player1 Received Message:", data)
    await sio.emit("my response", "A listener that was triggered by response")


@sio.event
async def move(data):
    print("Player 1 Received Move: ", data)


@sio.event
async def disconnect():
    print("Player 1 Disconnected from server")


async def main():
    await sio.connect("http://localhost:8000")
    while True:
        a_move = random.choice(["left", "right", "up", "down"])
        await sio.emit("move", a_move)
        sleep(1)

    await sio.wait()


if __name__ == "__main__":
    asyncio.run(main())


# while True:
#     a_move = random.choice(["left", "right", "up", "down"])
#     sio.emit(
#         "move",
#         a_move,
#     )
#     sleep(1)

# sio.wait()


# async def make_call():
#     while True:
#         a_move = random.choice(["left", "right", "up", "down"])
#         await sio.emit("move", a_move)
#         sleep(1)
