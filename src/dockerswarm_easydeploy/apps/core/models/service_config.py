from django.db import models


class ServiceEnvConfigModel(models.Model):
    env_item = models.ForeignKey("EvnItemModel", on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=254, null=True, blank=True, help_text="值")
    key = models.CharField(max_length=254, null=True, blank=True, help_text="使用新的名称")
    service = models.ForeignKey("ServiceConfigModel", on_delete=models.CASCADE)

    @property
    def real_value(self):
        if self.env_item:
            return self.env_item.value
        return self.env_item.value

class ServiceConfigModel(models.Model):
    host_name = models.CharField(max_length=100)
    stack = models.ForeignKey(
        "StackConfigModel",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_stateless = models.BooleanField(default=False)
    env_set = models.ManyToManyField(through=ServiceEnvConfigModel, to="EvnItemModel")

    image = models.CharField(max_length=254)
    deploy_policy = models.ForeignKey(
        "ServiceDeployPolicyModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
