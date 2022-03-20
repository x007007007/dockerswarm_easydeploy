import dataclasses
import typing
import grpc

from ..models import NodeModel
import docker_swarm_easy_deploy_proto_pb2_grpc as pb2_grpc
import docker_swarm_easy_deploy_proto_pb2 as pb2
from loguru import logger

@dataclasses.dataclass
class ReadDockerImageAction:

    node: NodeModel

    def filter_image_list(self):
        pass


