import datetime

from django.db import models


class NodeModel(models.Model):
    uuid = models.CharField(max_length=128)
    machine_id = models.CharField(max_length=254)
    group = models.ForeignKey("NodeGroupModel", related_name="node_set", on_delete=models.CASCADE)
    node_detail = models.JSONField(null=True, blank=True)
    client_port = models.IntegerField(null=True)
    client_addr = models.CharField(max_length=254, default='')
    last_update_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)


class NodeGroupModel(models.Model):
    name = models.CharField(max_length=250)