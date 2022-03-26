import pytest
import docker

from dockerswarm_easydeploy_client.image.image_info import iter_image_info_filter

docker_client = None


def setup_module(request):
    global docker_client
    docker_client = docker.client.from_env()


def test_image_info():
    assert isinstance(docker_client, docker.DockerClient)
    i = j = 0
    for i, image in enumerate(iter_image_info_filter(docker_client)):
        assert isinstance(image['id'], str)
        assert isinstance(image['history'], list)

    # for j, image in enumerate(iter_image_info_filter(docker_client, name='ubuntu')):
    #     assert isinstance(image['id'], str)
    #     assert isinstance(image['history'], list)
    # assert j < i