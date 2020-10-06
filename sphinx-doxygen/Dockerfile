FROM registry.gitlab.com/musicscience37_ci/clang-ci-docker:clang10-v2-2

ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        default-jre=2:1.11-72 \
        graphviz=2.42.2-3build2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv http://sourceforge.net/projects/plantuml/files/plantuml.1.2020.18.jar/download \
        -O ${PLANTUML_JAR_PATH} && \
    java -jar ${PLANTUML_JAR_PATH} -version

WORKDIR /usr/local/doxygen
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libtinfo5=6.2-0ubuntu2 \
        libclang1-9=1:9.0.1-12 \
        libclang-cpp9=1:9.0.1-12 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*
RUN wget -nv http://doxygen.nl/files/doxygen-1.8.20.linux.bin.tar.gz && \
    tar xf doxygen-1.8.20.linux.bin.tar.gz && \
    rm doxygen-1.8.20.linux.bin.tar.gz
ENV PATH=/usr/local/doxygen/doxygen-1.8.20/bin:$PATH

RUN pip3 install \
    sphinx==3.2.1 \
    breathe==4.22.1 \
    sphinxcontrib-plantuml==0.18.1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive=2019.20200218-1 \
        texlive-latex-recommended=2019.20200218-1 \
        texlive-fonts-recommended=2019.20200218-1 \
        texlive-font-utils=2019.202000218-1 \
        texlive-latex-extra=2019.202000218-1 \
        lmodern=2.004.5-6 \
        ghostscript=9.50~dfsg-5ubuntu4.2 \
        latexmk=1:4.67-0.1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /root
