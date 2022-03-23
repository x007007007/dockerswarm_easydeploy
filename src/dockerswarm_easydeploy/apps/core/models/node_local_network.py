from django.db import models


class NodeLocalNetworkModel(models.Model):
    node = models.ForeignKey("NodeModel", on_delete=models.CASCADE)
    network = models.ForeignKey("NetworkModel", on_delete=models.CASCADE)