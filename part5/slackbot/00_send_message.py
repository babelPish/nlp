import settings
from slacker import Slacker


slack = Slacker(settings.token)
slack.chat.post_message('#bot_test', 'Hello!')
