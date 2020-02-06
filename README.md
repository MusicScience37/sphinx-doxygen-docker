# sphinx-doxygen-docker

[![dockeri.co](https://dockeri.co/image/musicscience37/sphinx-doxygen)](https://hub.docker.com/r/musicscience37/sphinx-doxygen)

![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/musicscience37/sphinx-doxygen)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/musicscience37/sphinx-doxygen)

![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/MusicScience37/sphinx-doxygen-docker?label=latest)

[![pipeline status](https://gitlab.com/musicscience37_ci/sphinx-doxygen-docker/badges/develop/pipeline.svg)](https://gitlab.com/musicscience37_ci/sphinx-doxygen-docker/commits/develop)

Docker container image to build documentations using Sphinx and Doxygen supported by Breathe.

The container image in this project contains the following tools:

- Doxygen
- Sphinx
- Breathe
- PlantUML (path is set to an environment variable `PLANTUML_JAR_PATH`)
- TexLive

Test page is [here](https://musicscience37_ci.gitlab.io/sphinx-doxygen-docker/).

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37_ci/sphinx-doxygen-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37_ci/sphinx-doxygen-docker`
- [Docker Hub](https://hub.docker.com/r/musicscience37/sphinx-doxygen)
  - latest stable image: `musicscience37/sphinx-doxygen`

## Repositories

- [GitLab](https://gitlab.com/musicscience37_ci/sphinx-doxygen-docker):
  for development including CI
- [GitHub](https://github.com/MusicScience37/sphinx-docker):
  mirror repository for use in Docker Hub

## Test

To run a test of this project, execute the `run_test.sh` script.
It requires docker and docker-compose commands installed.
