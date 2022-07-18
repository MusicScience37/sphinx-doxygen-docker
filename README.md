# sphinx-doxygen-docker

[![dockeri.co](https://dockeri.co/image/musicscience37/sphinx-doxygen)](https://hub.docker.com/r/musicscience37/sphinx-doxygen)

[![pipeline status](https://gitlab.com/MusicScience37/sphinx-doxygen-docker/badges/main/pipeline.svg)](https://gitlab.com/MusicScience37/sphinx-doxygen-docker/-/commits/main)

Docker container image to build documentations using Sphinx and Doxygen supported by Breathe.

The container image in this project contains the following tools:

- Doxygen
- Sphinx
- Breathe
- PlantUML (path is set to an environment variable `PLANTUML_JAR_PATH`)
- TexLive

Test page is [here](https://musicscience37.gitlab.io/sphinx-doxygen-docker/).

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37/sphinx-doxygen-docker/container_registry)
  - latest stable image: `registry.gitlab.com/musicscience37/sphinx-doxygen-docker`
- [Docker Hub](https://hub.docker.com/r/musicscience37/sphinx-doxygen)
  - latest stable image: `musicscience37/sphinx-doxygen`

## Repositories

- [GitLab](https://gitlab.com/musicscience37/sphinx-doxygen-docker):
  for development including CI
- [GitHub](https://github.com/MusicScience37/sphinx-docker):
  mirror repository

## Testing

For test of this project,
use `./tool.py test` command.
