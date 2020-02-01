#!/bin/bash -e

pip3 install sphinx_rtd_theme==0.4.3

cd $(dirname $0)

rm -rf build
mkdir build
doxygen
sphinx-build -b html \
    sphinx build/sphinx/html \
    -D breathe_projects.TestBreathe="$(dirname $0)/build/doxygen/xml" \
    -D "plantuml=java -jar ${PLANTUML_JAR_PATH}"
