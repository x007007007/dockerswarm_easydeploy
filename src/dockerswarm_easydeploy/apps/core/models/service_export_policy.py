from django.db import models


class ServiceExportPolicyModel(models.Model):
    only_apply_for_service = models.ForeignKey(
        "ServiceConfigModel",
        null=True,
        on_delete=models.SET_NULL,
        blank=True
    )
    only_apply_for_stack = models.ForeignKey(
        "StackConfigModel",
        null=True,
        on_delete=models.SET_NULL,
        blank=True
    )