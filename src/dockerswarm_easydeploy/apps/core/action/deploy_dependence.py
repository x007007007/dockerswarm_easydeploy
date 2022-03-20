import dataclasses
import typing
import grpc

from ..models import StackConfigModel
import docker_swarm_easy_deploy_proto_pb2_grpc as pb2_grpc
import docker_swarm_easy_deploy_proto_pb2 as pb2
from loguru import logger



@dataclasses.dataclass
class DeployDependenceAction:


    def iter_deploy_network(self):
        

    def iter_deploy_service(self):
        pass


    def send_query(self):
        channel = grpc.insecure_channel('localhost:15005')
        client = pb2_grpc.DeployClientStub(channel)
        l = list(self.iter_deploy_service())
        logger.info(l)
        for i in client.update_service(iter(l)):
            logger.debug(i.status)