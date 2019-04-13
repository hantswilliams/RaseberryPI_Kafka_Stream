from kafka import KafkaConsumer

consumer = KafkaConsumer('console-test-topic', bootstrap_servers="ec2-54-213-227-230.us-west-2.compute.amazonaws.com:9092")
for msg in consumer:
    print (msg)