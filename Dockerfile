FROM debian:latest
WORKDIR /
RUN apt update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
COPY / /open-audio-controller
