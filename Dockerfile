FROM debian:latest
RUN apt update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
COPY . /open-audio-controller
WORKDIR /open-audio-controller
RUN pip3 install -r requirements.txt
WORKDIR tests
RUN coverage run test_suite.py
ENTRYPOINT ["coverage", "report"]
