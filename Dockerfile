FROM debian:latest
RUN apt update
RUN apt-get install -y python3-pip portaudio19-dev
RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /open-audio-controller
WORKDIR /open-audio-controller/tests
RUN coverage run test_suite.py
ENTRYPOINT ["coverage", "report"]
