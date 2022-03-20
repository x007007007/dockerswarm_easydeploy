import dataclasses
import grpc

from dockerswarm_easydeploy_proto import client_pb2_grpc as pb2_grpc
from loguru import logger



@dataclasses.dataclass
class DeployDependenceAction:


    def iter_deploy_network(self):
        pass

    def iter_deploy_service(self):
        pass


    def send_query(self):
        channel = grpc.insecure_channel('localhost:15005')
        client = pb2_grpc.DeployClientStub(channel)
        l = list(self.iter_deploy_service())
        logger.info(l)
        for i in client.update_service(iter(l)):
            logger.debug(i.status)