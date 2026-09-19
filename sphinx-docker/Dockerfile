ARG BASE_IMAGE
# Base image is set in tool.py. So left blank here intentionally.
FROM ${BASE_IMAGE}

# PlantUML
ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jre \
    graphviz \
    fonts-ipafont \
    fonts-ipaexfont \
    && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv https://github.com/plantuml/plantuml/releases/download/v1.2026.8/plantuml-1.2026.8.jar \
    -O ${PLANTUML_JAR_PATH}

#Doxygen
WORKDIR /usr/local/doxygen
RUN wget -nv https://github.com/doxygen/doxygen/releases/download/Release_1_18_0/doxygen-1.18.0.linux.bin.tar.gz && \
    tar xf doxygen-1.18.0.linux.bin.tar.gz && \
    rm doxygen-1.18.0.linux.bin.tar.gz
ENV PATH=/usr/local/doxygen/doxygen-1.18.0/bin:$PATH

# Tex
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-base \
    lmodern \
    ghostscript \
    latexmk \
    && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /root
