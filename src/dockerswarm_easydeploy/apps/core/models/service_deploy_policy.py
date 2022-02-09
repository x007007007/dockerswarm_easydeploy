from django.db import models


class ServiceDeployPolicyModel(models.Model):
    is_manager_only = models.BooleanField(default=False)
    is_work_only = models.BooleanField(default=False)
    is_privilege = models.BooleanField(default=False)