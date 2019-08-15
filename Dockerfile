FROM ubuntu:latest

# apt update and install
RUN apt update
RUN apt install -y mysql-server && apt install -y python3 && apt install -y python3-pip && apt install -y vim 

# pip install
RUN pip3 install mysql-connector-python

# for mysql
RUN service mysql start
RUN mysql_secure_installation
