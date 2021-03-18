FROM debian:latest
WORKDIR /
RUN apt update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
COPY / /open-audio-controller
RUN tests_passed=true
ENTRYPOINT ["python3", "/open-audio-controller/tests/open_audio_controller_test.py"]
