from django.db import models


class ServiceConfigModel(models.Model):
    service_type = models.CharField(
        choices=(
            ('container', 'container',),
            ('compose', 'compose'),
            ('stack', 'stack'),
        ),
        null=True,
        blank=True,
        editable=False,
        max_length=16
    )
    stack = models.ForeignKey(
        "StackConfigModel",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    host_name = models.CharField(max_length=100)
    image = models.CharField(max_length=254)
    deploy_policy = models.ForeignKey(
        "ServiceDeployPolicyModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )