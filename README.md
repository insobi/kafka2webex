# kafka2webex
This repository is an example to integrate both Apache Kafka and Cisco Webex Teams.
<br><br>

# prerequisites
- Webex Teams Account & Access Token
- Webex Teams Room
<br><br>

# Installation of Apache Kafka
TBD
<br><br>

# How to run
Update values properly in sample.properties.
```
[WEBEX]
ACCESS_TOKEN = CHANGE_ME
ROOM_ID = CHANGE_ME

[KAFKA]
URL = CHANGE_ME
TOPIC = CHANGE_ME
```

Then, create topic and write messages on the Kafka. For example,
```
cd {KAFKA_INSTALL_DIRECTORY}

bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

cat test.txt | bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
```

Then, run kakfa2webex.py.
```python
python kakfa2webex.py
```

Now, you can see result like below.

![webex](/images/webex.png)
<br><br>

# References
- https://webexteamssdk.readthedocs.io/en/latest/index.html
