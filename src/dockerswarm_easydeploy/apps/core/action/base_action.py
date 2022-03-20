import dataclasses
import grpc

from dockerswarm_easydeploy_proto import client_pb2_grpc as pb2_grpc
from loguru import logger


@dataclasses.dataclass
class BaseAction:

    def iter_deploy_network(self):
        return iter(())

    def iter_deploy_service(self):
        return iter(())

    def iter_deploy_config(self):
        return iter(())

    def iter_deploy_secure(self):
        return iter(())

    def iter_deploy_volume(self):
        return iter(())

    def send_query(self, client_host=None):
        if client_host is None:
            client_host = 'localhost:15005'
        channel = grpc.insecure_channel(client_host)
        client = pb2_grpc.DeployClientStub(channel)

        if n := list(self.iter_deploy_network()):
            logger.info(f"prepare network deploy: {n}")
            for r in client.create_network(self.iter_deploy_network()):
                print(r)

        if v := list(self.iter_deploy_volume()):
            logger.info(f"prepare volume deploy: {v}")
            client.create_volume(self.iter_deploy_volume())

        if c := list(self.iter_deploy_config()):
            logger.info(f"prepare config deploy: {c}")
            client.create_config(self.iter_deploy_volume())

        if s := list(self.iter_deploy_secure()):
            logger.info(f"prepare config deploy: {s}")
            client.create_secure(self.iter_deploy_secure())

        if serv := list(self.iter_deploy_service()):
            logger.info(f"prepare service deploy: {serv}")
            for res in client.update_service(self.iter_deploy_service()):
                logger.debug(res)
