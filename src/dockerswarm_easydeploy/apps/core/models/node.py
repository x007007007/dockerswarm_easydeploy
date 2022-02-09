from django.db import models


class NodeModel(models.Model):
    uuid = models.CharField(max_length=1000)
    group = models.ForeignKey("NodeGroupModel", related_name="node_set", on_delete=models.CASCADE)


class NodeGroupModel(models.Model):
    name = models.CharField(max_length=250)