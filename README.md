# sphinx-doxygen-docker

Docker container image to build documentations using Sphinx and Doxygen supported by Breathe.

The container image in this project contains the following tools:

- Doxygen
- Sphinx
- Breathe
- PlantUML (path is set to an environment variable `PLANTUML_JAR_PATH`)

Test page is [here](https://musicscience37_ci.gitlab.io/sphinx-doxygen-docker/).

## Container Registries

You can pull automatically built images from following registries:

- [GitLab Container Registry](https://gitlab.com/musicscience37_ci/sphinx-doxygen-docker/container_registry)

## Repositories

- [GitLab](https://gitlab.com/musicscience37_ci/sphinx-doxygen-docker):
  for development including CI

## Test

To run a test of this project, execute the `run_test.sh` script.
It requires docker and docker-compose commands installed.
