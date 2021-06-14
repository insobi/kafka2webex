from webexteamssdk import WebexTeamsAPI
import configparser

config = configparser.ConfigParser()
config.read('webex.properties')

WEBEX_TEAMS_ACCESS_TOKEN = config['WEBEX']['ACCESS_TOKEN']
WEBEX_TEAMS_ROOM_ID = config['WEBEX']['ROOM_ID']

MESSAGE = "Hello World!"

MARKDOWN = """
# Test Message
This is a sample message sent by webexteamssdk. Please refer to [this repo](https://github.com/insobi/kafka2webex).
<br>
## How to Run
```
python sample.py
```

## Markdown Example
- Buy a new shirt.
  * With buttons.
    * And a collar!
"""

api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)

message = api.messages.create(WEBEX_TEAMS_ROOM_ID, text=MESSAGE)
message = api.messages.create(WEBEX_TEAMS_ROOM_ID, markdown=MARKDOWN)