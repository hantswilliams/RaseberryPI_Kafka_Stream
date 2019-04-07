from kafka import KafkaProducer
import time
import json

#NOTE - need to run this example in Python 2.7

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(100):
    dict = {}
    dict['name_'+str(i)] = 'FILE_' + str(i)
    dict['size_'+str(i)] = '23.' + str(i)
    dict['host_'+str(i)] = '10.0.0.0' + str(i)
    jd = json.dumps(dict)
    producer.send('console-test-topic', jd)
    time.sleep(2)