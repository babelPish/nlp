import settings
import requests
import json
import asyncio
import websockets
import slacker


slack = slacker.Slacker(settings.token)
slack.chat.post_message('#bot_test', 'Hello!')

response = requests.get('https://slack.com/api/rtm.start', dict(token=settings.token))
endpoint = response.json()['url']

async def hello():
    ws = await websockets.connect(endpoint)
    while True:
        raw_msg = await ws.recv()
        msg = json.loads(raw_msg)

        print(msg)

        if msg['type'] == 'message' and msg['text'].startswith('give'):
            cmd, arg = msg['text'].split(' ', 1)

            slack.reactions.add(arg, channel=msg['channel'], timestamp=msg['ts'])


asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
