# test-Jenkins-
For tests :0

## Jenkins 
sudo apt-get default-jdk
sudo wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt update

sudo apt install jenkins

sudo systemctl start jenkins


## RSA SSH on Worker
sudo apt-get default-jdk
cd ~/.ssh/ && ssh-keygen -t rsa
cat id_rsa.pub>>authorized_keys
cat id_rsa
