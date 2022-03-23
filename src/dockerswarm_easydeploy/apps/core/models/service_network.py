from django.db import models


class ServiceNetworkModel(models.Model):
    service = models.ForeignKey("ServiceConfigModel", on_delete=models.CASCADE)
    network = models.ForeignKey("NetworkModel", on_delete=models.CASCADE)