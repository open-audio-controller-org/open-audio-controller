
test:
	docker build -t open-audio-controller .
	docker run -it open-audio-controller

.PHONY: test