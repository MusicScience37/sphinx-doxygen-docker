#!/bin/bash -e

# run test of this project

compose_file=$(dirname $0)/sphinx-doxygen/docker-compose.test.yml
docker-compose -f $compose_file up --build
docker-compose -f $compose_file down
