.PHONY: build run debug

build:
	docker build -t webimage .

run:
	docker run -d --name web -p 8000:8000 webimage

debug:
	docker run --rm -a stderr -p 8000:8000 --name webdebug webimage 
