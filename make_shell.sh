#!/bin/bash -e

# this is a shell script to build an image and make a shell from the image

docker build -t sphinx-docker sphinx-docker
docker run --rm -it sphinx-docker bash
