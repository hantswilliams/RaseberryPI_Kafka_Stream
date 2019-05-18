# Raseberrypi_Kafka_Stream

## Purpose
This is a template for creating a MVP model of sending a live video
stream from a RaseberryPi3, to WWW for 'anywhere' viewing - all local 
off of the Pi - no ec2, no cloud - just the Pi 


## Connecting to Raseberry Pi / Setup 
On the raseberrypi, be sure to enable the cv2.VideoCapture ability by performing: <br>
```sudo modprobe bcm2835-v4l2``` 
<br> In addition, to start the proper python binders (if using Adrian OS image) by sure to perform <br>
```source start_py3cv3.sh``` 
<br> Once ready to begin, get the producer.py setup and running (ensuring zookeeper and kafka are running first) <br>
Then perform the below command to get consumer working:  <br>
```gunicorn app:app -b 127.0.0.1:8001``` 
<br> Refer to the nginx file if changes need to get made, but otherwise you are then good to go! 







## For the producer/consumer to work:
make sure that the producer is sending the data its own machine, while have the listening - inserting in the IP address of the producer machine - might need to create a static IP / public address via the router for EC2 to find the address


## ZOOKEEPER + KAFKA INSTALLATION 
```
https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd <br>
https://linuxhint.com/install-apache-kafka-ubuntu/ <br>
install java first <br>
first check to see if you have Java JDK 8 - with (e.g., raseberry pi already installed) <br>
java -version<br>
#If not, then do: <br>
	sudo add-apt-repository -y ppa:webupd8team/java <br>
	sudo apt-get update <br>
	sudo apt-get install oracle-java8-installer -y <br>
Now install zookeeper <br>
sudo apt-get install zookeeperd #install zookeeper <br>
sudo systemctl status zookeeper #make sure its running  <br>
sudo systemctl enable zookeeper #enable zookepper running at startup  <br>
#navigate to downloads  <br>
cd <br> 
mkdir downloads <br>
cd downloads <br>
wget ftp://apache.cs.utah.edu/apache.org/kafka/2.2.0/kafka_2.12-2.2.0.tgz <br>
sudo mkdir /opt/Kafka <br>
sudo tar xvzf kafka_2.12-1.0.0.tgz -C /opt/Kafka  ##note, change the 1.0.0 to 2.2.0 or watever version is being utilized <br>
##to start up kafka manually  <br>
cd /opt/Kafka/kafka_2.11-1.0.1/ <br>
sudo bin/kafka-server-start.sh config/server.properties <br>
##to test that it is working properly <br>
cd /opt/Kafka/kafka_2.11-1.0.1/ <br>
#Then create a testing topic <br>
sudo bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing <br>
```
