import settings
import requests
import websocket


response = requests.get('https://slack.com/api/rtm.start', dict(token=settings.token))
endpoint = response.json()['url']

s = websocket.create_connection(endpoint)
while True:
    msg = s.recv()
    print(msg)
