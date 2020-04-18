FROM registry.gitlab.com/musicscience37_ci/clang-ci-docker:clang9-v1-1

ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        default-jre=2:1.11-72 \
        graphviz=2.40.1-7build1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv http://sourceforge.net/projects/plantuml/files/plantuml.1.2020.5.jar/download \
        -O ${PLANTUML_JAR_PATH} && \
    java -jar ${PLANTUML_JAR_PATH} -version

WORKDIR /usr/local/doxygen
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libtinfo5=6.1+20190803-1ubuntu1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*
RUN wget -nv http://doxygen.nl/files/doxygen-1.8.18.linux.bin.tar.gz && \
    tar xf doxygen-1.8.18.linux.bin.tar.gz && \
    rm doxygen-1.8.18.linux.bin.tar.gz
ENV PATH=/usr/local/doxygen/doxygen-1.8.18/bin:$PATH

RUN pip3 install \
    sphinx==2.4.4 \
    breathe==4.14.1 \
    sphinxcontrib-plantuml==0.18

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive=2019.20190710-1 \
        texlive-latex-recommended=2019.20190710-1 \
        texlive-fonts-recommended=2019.20190710-1 \
        texlive-font-utils=2019.20190710-1 \
        texlive-latex-extra=2019.20190710-1 \
        lmodern=2.004.5-6 \
        ghostscript=9.27~dfsg+0-0ubuntu3.1 \
        latexmk=1:4.65-0.2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /root
