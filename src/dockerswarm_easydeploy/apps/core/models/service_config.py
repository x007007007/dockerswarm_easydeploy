from django.db import models


class ServiceConfigModel(models.Model):

    host_name = models.CharField(max_length=100)

    stack = models.ForeignKey(
        "StackConfigModel",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_stateless = models.BooleanField(default=False)

    image = models.CharField(max_length=254)
    deploy_policy = models.ForeignKey(
        "ServiceDeployPolicyModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
