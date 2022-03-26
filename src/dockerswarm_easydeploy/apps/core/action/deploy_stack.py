import dataclasses
import typing
import grpc

from ..models import StackConfigModel
from dockerswarm_easydeploy_proto import client_pb2 as pb2, \
    client_pb2_grpc as pb2_grpc
from loguru import logger
from .base_action import BaseAction


@dataclasses.dataclass
class DeployStackAction(BaseAction):
    obj: StackConfigModel

    def get_export_labels(self) -> typing.Dict:
        return dict(

        )

    def get_export_network_config(self) -> typing.List[str]:
        return [
            'traefik-public'
        ]

    def get_deploy_constraint(self):
        return {
        }

    def iter_deploy_service(self):
        for service in self.obj.serviceconfigmodel_set.all():
            logger.debug(f"deploy service: {service.stack.name}>{service.host_name}")
            yield pb2.ServiceConfig(
                name=f"{service.stack.name}_{service.host_name}",
                container=pb2.BasicContainerRunConfig(
                    image=service.image.get_image_url(),
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

