FROM debian:latest
RUN apt update
RUN apt-get install -y python3-pip portaudio19-dev
RUN pip3 install --upgrade pip
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app
# WORKDIR /open-audio-controller/tests
# RUN coverage run test_suite.py
# ENTRYPOINT ["coverage", "report"]
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["open_audio_controller/__open-audio-flask__.py"]