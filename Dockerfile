FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y --no-install-recommends \
    	install \
	build-essential \
	curl \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	libffi-dev \
	git && \
    apt-get clean


