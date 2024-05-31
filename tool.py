#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2022 Kenta Kabashima
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""Tool to create and test Docker image.
"""

import datetime
import os
import subprocess

import click

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

GITLAB_IMAGE_URL = (
    "registry.gitlab.com/musicscience37projects/docker/sphinx-doxygen-docker"
)
DOCKER_HUB_IMAGE_URL = "musicscience37/sphinx-doxygen"

IMAGE_TAGS = [
    "clang15",
    "clang16",
    "clang17",
    "clang18",
    "clang19",
    "gcc12",
    "gcc13",
]
LATEST_IMAGE_TAG = "clang17"

DOCKERFILE_DIR_NAME = "sphinx-docker"


@click.group()
def cli():
    pass


def _run_command(command: list[str]):
    """Run a command.

    Args:
        command (list[str]): Command.
    """

    click.secho(f"> {command}", bold=True)
    subprocess.run(command, check=True, cwd=THIS_DIR)


def _create_time_stamp() -> str:
    """Create a time stamp.

    Returns:
        str: Time stamp.
    """

    return datetime.datetime.now().strftime("%Y%m%d")


def _select_base_image(tag_name: str) -> str:
    if tag_name.startswith("clang"):
        return f"musicscience37/clang-ci:{tag_name}"
    if tag_name.startswith("gcc"):
        return f"musicscience37/gcc-ci:{tag_name}"
    raise ValueError("Invalid tag.")


def _build(tag_name: str, image_full_name: str):
    """Build Docker image.

    Args:
        tag_name (str): Tag of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "build",
            "-t",
            image_full_name,
            "--build-arg",
            f"BASE_IMAGE={_select_base_image(tag_name)}",
            DOCKERFILE_DIR_NAME,
        ]
    )


def _test(image_full_name: str):
    """Test Docker image.

    Args:
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{THIS_DIR}/test:/home/test",
            image_full_name,
            "/home/test/run_test.sh",
        ]
    )


def _tag_and_upload(image_full_name: str, another_image_full_name: str):
    _run_command(["docker", "tag", image_full_name, another_image_full_name])
    _run_command(["docker", "push", another_image_full_name])


def _upload(tag_name: str, image_full_name: str):
    """Upload Docker image.

    Args:
        tag_name (str): Tag of the image.
        image_full_name (str): Full name of the image.
    """

    _run_command(
        [
            "docker",
            "login",
            "-u",
            os.environ["CI_REGISTRY_USER"],
            "-p",
            os.environ["CI_REGISTRY_PASSWORD"],
            os.environ["CI_REGISTRY"],
        ]
    )
    _run_command(["docker", "push", image_full_name])
    _tag_and_upload(
        image_full_name=image_full_name,
        another_image_full_name=f"{GITLAB_IMAGE_URL}:{tag_name}-{_create_time_stamp()}",
    )
    if tag_name == LATEST_IMAGE_TAG:
        _tag_and_upload(
            image_full_name=image_full_name,
            another_image_full_name=f"{GITLAB_IMAGE_URL}:latest",
        )

    _run_command(
        [
            "docker",
            "login",
            "-u",
            os.environ["HUB_USER_NAME"],
            "-p",
            os.environ["HUB_ACCESS_TOKEN"],
        ]
    )
    _tag_and_upload(
        image_full_name=image_full_name,
        another_image_full_name=f"{DOCKER_HUB_IMAGE_URL}:{tag_name}",
    )
    if tag_name == LATEST_IMAGE_TAG:
        _tag_and_upload(
            image_full_name=image_full_name,
            another_image_full_name=f"{DOCKER_HUB_IMAGE_URL}:latest",
        )


@cli.command()
@click.argument("tag_name", type=click.Choice(IMAGE_TAGS))
def test(tag_name: str):
    """Build and test Docker image."""

    image_full_name = f"{GITLAB_IMAGE_URL}:{tag_name}-test"
    _build(tag_name=tag_name, image_full_name=image_full_name)
    _test(image_full_name=image_full_name)


@cli.command()
@click.argument("tag_name", type=click.Choice(IMAGE_TAGS))
def update(tag_name: str):
    """Build and test Docker image."""

    image_full_name = f"{GITLAB_IMAGE_URL}:{tag_name}"
    _build(tag_name=tag_name, image_full_name=image_full_name)
    _test(image_full_name=image_full_name)
    _upload(tag_name=tag_name, image_full_name=image_full_name)


if __name__ == "__main__":
    cli()
