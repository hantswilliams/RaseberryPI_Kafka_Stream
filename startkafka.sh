#!/bin/bash
cd 
cd /opt/Kafka/kafka_2.12-2.2.0/
sudo bin/kafka-server-start.sh config/server.properties & echo $! kafka_pid.txt
