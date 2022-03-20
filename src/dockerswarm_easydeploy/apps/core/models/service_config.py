import typing

from django.db import models
from loguru import logger

class ServiceConfigModel(models.Model):
    host_name = models.CharField(max_length=100)
    stack = models.ForeignKey(
        "StackConfigModel",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    service_id = models.CharField(max_length=254, editable=False)
    is_stateless = models.BooleanField(default=False)
    env_set = models.ManyToManyField(through="ServiceEnvConfigModel", to="EvnItemModel")
    port_set = models.ManyToManyField(through="ServicePortConfigModel", to="ServiceExportPolicyItemModel")
    image = models.CharField(max_length=254)
    deploy_policy = models.ForeignKey(
        "ServiceDeployPolicyModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cmds = models.TextField(default="", blank=True, help_text="一个命令一行,同Args")
    entrypoint = models.TextField(default="", blank=True, help_text="入口")


    def __str__(self):
        return f"<{self.__class__.__name__} ({self.pk}) hn:{self.host_name} i:{self.image}>"

    def get_port_map(self) -> typing.Dict[str, str]:
        from .service_export_policy_item import ServiceExportPolicyItemModel
        res = {}
        for port_config in self.serviceportconfigmodel_set.filter(
                export_policy__protocol__in=(
                    ServiceExportPolicyItemModel.TYPE_TCP,
                    ServiceExportPolicyItemModel.TYPE_UDP,
                    ServiceExportPolicyItemModel.TYPE_TCP_UDP,
                )
            ).all():
            inner_port = port_config.inner_port or port_config.export_policy.inner_port
            res[f"{port_config.export_policy.port!s}"] = f"{inner_port!s}"
        logger.debug(f"get port map: {res}")
        return res