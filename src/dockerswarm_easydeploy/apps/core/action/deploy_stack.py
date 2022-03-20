import dataclasses
import typing
import grpc

from ..models import StackConfigModel
import docker_swarm_easy_deploy_proto_pb2_grpc as pb2_grpc
import docker_swarm_easy_deploy_proto_pb2 as pb2
from loguru import logger


@dataclasses.dataclass
class DeployStackAction:
    obj: StackConfigModel

    def get_export_labels(self) -> typing.Dict:
        return dict(

        )

    def get_export_network_config(self) -> typing.List[str]:
        return [
            'traefik'
        ]

    def get_deploy_constraint(self):
        return {
        }

    def iter_deploy_service(self):
        for service in self.obj.serviceconfigmodel_set.all():
            yield pb2.ServiceConfig(
                name=f"{service.stack.name}_{service.host_name}",
                container=pb2.BasicContainerRunConfig(
                    image=service.image,
                    cmds=[],
                    entrypoints=[],
                    envs={},
                    ports={},
                    label={
                        **self.get_export_labels()
                    },
                    networks=[
                        *self.get_export_network_config()
                    ]
                ),
                config={},
                constraint=pb2.DeployConstraintConfig(
                    placement_eq_constraint={
                        **self.get_deploy_constraint()
                    }
                )
            )

    def send_query(self):
        channel = grpc.insecure_channel('localhost:15005')
        client = pb2_grpc.DeployClientStub(channel)
        l = list(self.iter_deploy_service())
        logger.info(l)
        for i in client.update_service(iter(l)):
            logger.debug(i.status)