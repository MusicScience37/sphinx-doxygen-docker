FROM musicscience37/clang-ci:clang14-v4.3

# PlantUML
ENV PLANTUML_JAR_PATH="/usr/local/plantuml/plantuml.jar"
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-jre=2:1.11-72 \
    graphviz=2.42.2-3build2 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/* && \
    mkdir -p /usr/local/plantuml && \
    wget -nv http://sourceforge.net/projects/plantuml/files/plantuml.1.2022.4.jar/download \
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
    sphinx==4.5.0 \
    breathe==4.33.1 \
    sphinxcontrib-plantuml==0.23 && \
    # Tex
    apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive=2019.20200218-1 \
    texlive-latex-recommended=2019.20200218-1 \
    texlive-fonts-recommended=2019.20200218-1 \
    texlive-font-utils=2019.202000218-1 \
    texlive-latex-extra=2019.202000218-1 \
    lmodern=2.004.5-6 \
    ghostscript=9.50~dfsg-5ubuntu4.5 \
    latexmk=1:4.67-0.1 \
    fonts-ipafont=00303-18ubuntu1 && \
    apt-get autoremove && \
    apt-get autoclean && \
    rm -r /var/lib/apt/lists/*

WORKDIR /root
