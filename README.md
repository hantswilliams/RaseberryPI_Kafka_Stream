Raseberrypi_Kafka_Stream

####Purpose
<p> This is a template for creating a MVP model of sending a live video
stream from a RaseberryPi3, to a AWS EC2 instance for 'anywhere' viewing </p>


###Connecting to Raseberry Pi / Setup 
<p> For now, currently testing with Ubuntu Core - termninal only. Google for instrucitons on how to download
the OS - high level - using etcher to burn OS to SD card, then having ubuntu core account setup with public key 
availble for remote SSH access </p>
<br>
<p> Currently the IP is 172.16.75.156 / so would be ssh hants@172.16.75.156 </p>

#Step 1 - Install Core Developer Tools 
#Check out this https://developer.ubuntu.com/core/get-started/developer-setup
#Will need to run commands like: 
snap install classic --edge --devmode
sudo classic
#then can do: 
sudo apt update
