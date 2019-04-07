Raseberrypi_Kafka_Stream

####Purpose
<p> This is a template for creating a MVP model of sending a live video
stream from a RaseberryPi3, to a AWS EC2 instance for 'anywhere' viewing </p>


###Connecting to Raseberry Pi / Setup 
On the raseberrypi, be sure to enable the cv2.VideoCapture ability by performing:
```sudo modprobe bcm2835-v4l2```


###ZOOKEEPER + KAFKA INSTALLATION 
#https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd
#https://linuxhint.com/install-apache-kafka-ubuntu/
#install java first 
<p>
#first check to see if you have Java JDK 8 - with (e.g., raseberry pi already installed)
java -version
#If not, then do: 
	sudo add-apt-repository -y ppa:webupd8team/java
	sudo apt-get update
	sudo apt-get install oracle-java8-installer -y
#Now install zookeeper
sudo apt-get install zookeeperd #install zookeeper
sudo systemctl status zookeeper #make sure its running 
sudo systemctl enable zookeeper #enable zookepper running at startup 
#navigate to downloads 
cd 
mkdir downloads 
cd downloads 
wget ftp://apache.cs.utah.edu/apache.org/kafka/2.2.0/kafka_2.12-2.2.0.tgz
sudo mkdir /opt/Kafka
sudo tar xvzf kafka_2.12-1.0.0.tgz -C /opt/Kafka  ##note, change the 1.0.0 to 2.2.0 or watever version is being utilized
##to start up kafka manually 
cd /opt/Kafka/kafka_2.11-1.0.1/
sudo bin/kafka-server-start.sh config/server.properties
##to test that it is working properly 
cd /opt/Kafka/kafka_2.11-1.0.1/
sudo bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing
</p>