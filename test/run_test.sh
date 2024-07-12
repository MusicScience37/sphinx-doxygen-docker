#!/bin/bash -e

set -e

pip3 install sphinx_rtd_theme==1.0.0

cd $(dirname $0)

rm -rf build
mkdir build
doxygen

sphinx-build -M html \
    sphinx build/sphinx \
    -D breathe_projects.TestBreathe="$(dirname $0)/build/doxygen/xml" \
    -D "plantuml=java -jar ${PLANTUML_JAR_PATH}"
