#!/bin/bash
cd 
cd /opt/Kafka/kafka_2.11-1.0.1/
sudo bin/kafka-server-start.sh config/server.properties & echo $! kafka_pid.txt
