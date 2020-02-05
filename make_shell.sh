#!/bin/bash -e

# this is a shell script to build an image and make a shell from the image

docker build -t sphinx-doxygen sphinx-doxygen
docker run --rm -it sphinx-doxygen bash
