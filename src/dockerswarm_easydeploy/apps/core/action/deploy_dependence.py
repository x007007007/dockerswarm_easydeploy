import dataclasses
import grpc

from dockerswarm_easydeploy_proto import client_pb2_grpc as pb2_grpc
from dockerswarm_easydeploy_proto import client_pb2 as pb2
from loguru import logger
from .base_action import BaseAction
from .deploy_stack import DeployStackAction
from dockerswarm_easydeploy.apps.core.models import (
    StackConfigModel,
    ServiceConfigModel,
)

class DeployDependenceAction(DeployStackAction):

    def iter_deploy_network(self):
        yield pb2.NetworkConfig(
            name="traefik-public",
            driver="overlay",
            scope="swarm",
            options={},
            labels={},
            attachable=True,
        )

    def iter_deploy_service(self):
        for service in ServiceConfigModel.objects.filter(stack__in=StackConfigModel.objects.inner()):  # type: ServiceConfigModel
            logger.debug(f"deploy inner service: {service.stack.name}>{service.host_name}")
            yield pb2.ServiceConfig(
                    name=f"{service.stack.name}_{service.host_name}",
                    container=pb2.BasicContainerRunConfig(
                        image=service.image,
                        cmds=[],
                        entrypoints=[],
                        envs={},
                        ports=service.get_port_map(),
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


