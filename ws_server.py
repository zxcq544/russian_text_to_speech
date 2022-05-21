import asyncio
import websockets
from say_neural import NeuralSpeaker

neural_speaker = NeuralSpeaker()


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        print(f': {message}')
        neural_speaker.speak(message)


async def main():
    async with websockets.serve(handler, "", 8001, ping_interval=None):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
