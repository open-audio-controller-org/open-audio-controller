

.PHONY: test build

build:
	docker build -t open-audio-controller .
	docker run --env FLASK_APP=open_audio_controller/open_audio_flask.py -it open-audio-controller

test:
	docker build -f Dockerfile_test -t open-audio-controller .
	docker run --env FLASK_APP=open_audio_controller/open_audio_flask.py -it open-audio-controller


default: build	