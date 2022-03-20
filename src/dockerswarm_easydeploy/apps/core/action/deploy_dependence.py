import dataclasses
import grpc

from dockerswarm_easydeploy_proto import client_pb2_grpc as pb2_grpc
from dockerswarm_easydeploy_proto import client_pb2 as pb2
from loguru import logger



@dataclasses.dataclass
class DeployDependenceAction:


    def iter_deploy_network(self):
        yield pb2.NetworkConfig(
            name="traefik-public",
            driver="overlay",
            scope="swarm",
            attachable=True,
            ingress=True
        )

    def iter_deploy_service(self):
        if False:
            yield None
        return

    def send_query(self):
        channel = grpc.insecure_channel('localhost:15005')
        client = pb2_grpc.DeployClientStub(channel)
        n = list(list(self.iter_deploy_network()))
        logger.info(f"network deploy: {n}")
        client.create_network(self.iter_deploy_network())
        l = list(self.iter_deploy_service())
        logger.info(f"service deploy: {l}")

