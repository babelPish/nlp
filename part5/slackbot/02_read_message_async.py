import settings
import requests
import asyncio
import websockets


response = requests.get('https://slack.com/api/rtm.start', dict(token=settings.token))
endpoint = response.json()['url']

async def hello():
    ws = await websockets.connect(endpoint)
    while True:
        msg = await ws.recv()
        print(msg)

asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
