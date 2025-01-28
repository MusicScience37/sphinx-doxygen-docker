#!/bin/bash -e

set -e

cd $(dirname $0)

poetry install

rm -rf build
mkdir build
doxygen

poetry run sphinx-build -M html \
    sphinx build/sphinx \
    -D breathe_projects.TestBreathe="$(dirname $0)/build/doxygen/xml" \
    -D "plantuml=java -jar ${PLANTUML_JAR_PATH}"
