FROM musicscience37/clang-ci:clang13-v4.0

# PlantUML
ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jre=2:1.11-72build1 \
    graphviz=2.42.2-5build1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv http://sourceforge.net/projects/plantuml/files/plantuml.1.2022.1.jar/download \
    -O ${PLANTUML_JAR_PATH} && \
    java -jar ${PLANTUML_JAR_PATH} -version

#Doxygen
WORKDIR /usr/local/doxygen
RUN wget -nv http://doxygen.nl/files/doxygen-1.9.3.linux.bin.tar.gz && \
    tar xf doxygen-1.9.3.linux.bin.tar.gz && \
    rm doxygen-1.9.3.linux.bin.tar.gz
ENV PATH=/usr/local/doxygen/doxygen-1.9.3/bin:$PATH

# Sphinx
RUN pip3 install --no-cache-dir \
    sphinx==4.4.0 \
    breathe==4.32.0 \
    sphinxcontrib-plantuml==0.22 && \
    # Tex
    apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive=2021.20220204-1 \
    texlive-latex-recommended=2021.20220204-1 \
    texlive-fonts-recommended=2021.20220204-1 \
    texlive-font-utils=2021.20211217-1 \
    texlive-latex-extra=2021.20211217-1 \
    lmodern=2.004.5-6.1 \
    ghostscript=9.55.0~dfsg1-0ubuntu4 \
    latexmk=1:4.76-1 \
    fonts-ipafont=00303-21ubuntu1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /root
