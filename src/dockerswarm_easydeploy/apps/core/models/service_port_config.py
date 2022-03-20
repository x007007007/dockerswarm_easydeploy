from django.db import models


class ServicePortConfigModel(models.Model):
    """
    跟着image走
    """
    is_image_cnf = models.BooleanField(default=False, editable=False)
    export_policy = models.ForeignKey("ServiceExportPolicyItemModel", null=True, blank=True, on_delete=models.SET_NULL)
    service = models.ForeignKey("ServiceConfigModel", on_delete=models.CASCADE)
    inner_port = models.IntegerField()

