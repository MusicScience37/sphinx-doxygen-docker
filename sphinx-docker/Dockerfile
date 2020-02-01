FROM registry.gitlab.com/musicscience37_ci/cpp-base-image-docker:v0-1

ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        default-jre=2:1.11-72 \
        graphviz=2.40.1-7build1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv http://sourceforge.net/projects/plantuml/files/plantuml.1.2020.0.jar/download \
        -O ${PLANTUML_JAR_PATH} && \
    java -jar ${PLANTUML_JAR_PATH} -version

WORKDIR /usr/local/doxygen
RUN wget -nv http://doxygen.nl/files/doxygen-1.8.16.linux.bin.tar.gz && \
    tar xf doxygen-1.8.16.linux.bin.tar.gz && \
    rm doxygen-1.8.16.linux.bin.tar.gz
ENV PATH=/usr/local/doxygen/doxygen-1.8.16/bin:$PATH

RUN pip3 install \
    sphinx==2.3.1 \
    breathe==4.14.0 \
    sphinx_rtd_theme==0.4.3 \
    sphinxcontrib-plantuml==0.18
