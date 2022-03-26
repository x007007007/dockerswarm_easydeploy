import docker
from loguru import logger
import fnmatch


def iter_image_info_filter(client: docker.DockerClient, name=None):

    for image in client.images.list():
        if name:
            if len(fnmatch.filter(image.tags, name)) == 0:
                logger.debug(f"skip {image.short_id} {image.attrs['RepoTags']}")
                continue
        yield dict(
            id=image.id,
            attrs=image.attrs,
            tags=image.tags,
            labels=image.labels,
            history=image.history()
        )
