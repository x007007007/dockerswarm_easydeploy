import dataclasses
import json
import typing

from loguru import logger

import grpc
from dockerswarm_easydeploy_proto import client_pb2 as pb2, \
    client_pb2_grpc as pb2_grpc

from ..models import NodeModel
from ..models import ImageModel
from ..models import ImageSerialNodel
from ..models import ImageTagModel
from ..models import ImageEnvModel
from ..models import ImageRepoModel


@dataclasses.dataclass
class ReadDockerImageAction:

    node: NodeModel

    def update_image_info(self, image_info: pb2.ImageInfo) -> (typing.Optional[ImageModel], bool):
        attrs = json.loads(image_info.attr_json)
        history = json.loads(image_info.history_json)

        logger.debug(f"image attrs: {attrs}")

        env_list = []
        for item in attrs['Config']['Env']:
            env_list.append(item.split("=", maxsplit=1))
        env = dict(env_list)

        if not (select_name := attrs['RepoTags']):
            logger.debug("no repo tags")
            return None, False
        select_name = select_name[0]
        is_create = False
        if (image := ImageModel.objects.filter(hash=image_info.id).first()) is None:
            image, is_create = ImageModel.objects.update_or_create(
                defaults=dict(
                    name=ImageSerialNodel.objects.create(name=select_name),
                    entrypoint=attrs['Config'].get("Entrypoint") or [],
                    cmds=attrs['Config'].get("Cmd") or [],
                    user=attrs['Config'].get("User") or '',
                    work_dir=attrs['Config']["WorkingDir"] or '',
                    history=history
                ),
                hash=image_info.id
            )
        image.update_env_list(env)

        return image, is_create

    def iter_send_query(self, name=None, client_host=None) -> typing.List[ImageModel]:
        if client_host is None:
            client_host = self.node.get_client_connect_str()
        res = []
        with grpc.insecure_channel(client_host) as channel:
            client = pb2_grpc.DeployClientStub(channel)

            for r in client.iter_image_info_filter(pb2.ImageFilter()):
                if image_with_status := self.update_image_info(r):
                    yield image_with_status

