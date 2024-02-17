ARG BASE_TAG
FROM musicscience37/clang-ci:${BASE_TAG}

# PlantUML
ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jre \
    graphviz \
    fonts-ipafont \
    && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv https://github.com/plantuml/plantuml/releases/download/v1.2024.3/plantuml-1.2024.3.jar \
    -O ${PLANTUML_JAR_PATH}

#Doxygen
WORKDIR /usr/local/doxygen
RUN wget -nv https://www.doxygen.nl/files/doxygen-1.10.0.linux.bin.tar.gz && \
    tar xf doxygen-1.10.0.linux.bin.tar.gz && \
    rm doxygen-1.10.0.linux.bin.tar.gz
ENV PATH=/usr/local/doxygen/doxygen-1.10.0/bin:$PATH

# Sphinx
RUN pip3 install --no-cache-dir \
    sphinx \
    breathe \
    sphinxcontrib-plantuml && \
    # Tex
    apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    texlive-font-utils \
    texlive-latex-extra \
    lmodern \
    ghostscript \
    latexmk \
    && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /root
