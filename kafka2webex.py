from confluent_kafka import Consumer
from webexteamssdk import WebexTeamsAPI
import configparser

config = configparser.ConfigParser()
config.read('sample.properties')

WEBEX_TEAMS_ACCESS_TOKEN = config['WEBEX']['ACCESS_TOKEN']
WEBEX_TEAMS_ROOM_ID = config['WEBEX']['ROOM_ID']
KAFKA_BOOTSTRAP_SERVER = config['KAFKA']['BOOTSTRAP_SERVER']
KAFKA_TOPIC = config['KAFKA']['TOPIC']

c = Consumer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVER,
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe([KAFKA_TOPIC])

api = WebexTeamsAPI(access_token=WEBEX_TEAMS_ACCESS_TOKEN)

print("Wating messages...")
while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    MESSAGE = msg.value().decode('utf-8')
    print('Received message: {}'.format(MESSAGE))
    print(api.messages.create(WEBEX_TEAMS_ROOM_ID, text=MESSAGE))

c.close()