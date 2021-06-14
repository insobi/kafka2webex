from webexteamssdk import WebexTeamsAPI

# Import from environment variable
WEBEX_TEAMS_ACCESS_TOKEN = "NWE0NDBkNTItYjUzYy00ZGRmLWFhOGItNjhiNDBkNTRiNmZmYzhkNzZlNjAtYWMy_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
ROOM_ID="Y2lzY29zcGFyazovL3VzL1JPT00vOGZjYTVlOTAtNWZmNi0xMWViLWI3OTYtZDU3ZWIzN2E0NWFi"

api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)

# get list of rooms
rooms = api.rooms.list()
for room in rooms:
    print(room.title)
    print(room.id)
    print("---")

message = api.messages.create(ROOM_ID, text="sended by kafka2webex...")