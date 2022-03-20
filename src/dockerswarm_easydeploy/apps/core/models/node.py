import datetime

from django.db import models


class NodeModel(models.Model):
    display_name = models.CharField(max_length=64, default='')
    uuid = models.CharField(max_length=128, unique=True)
    machine_id = models.CharField(max_length=254)
    group = models.ForeignKey("NodeGroupModel", related_name="node_set", on_delete=models.CASCADE)
    node_detail = models.JSONField(null=True, blank=True)
    client_port = models.IntegerField(null=True)
    client_addr = models.CharField(max_length=254, default='')
    last_update_time = models.DateTimeField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    is_enable = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    manage_point = models.ForeignKey(
        "NodeManagePointModel",
        on_delete=models.SET_NULL,
        null=True
    )

    @property
    def is_swarm_node(self):
        if self.swarm_node_id:
            return True
        return False

    @property
    def swarm_node_id(self):
        return self.node_detail.get('Swarm', {}).get('NodeID')

    @property
    def is_swarm_manager(self):
        return self.node_detail.get("Swarm", {}).get("ControlAvailable", False)


class NodeManagePointModel(models.Model):
    TYPE_SWARM = 'swarm'
    TYPE_STANDALONE = 'standalone'
    type = models.CharField(
        choices=(
            (TYPE_SWARM, TYPE_SWARM),
            (TYPE_STANDALONE, TYPE_STANDALONE),
        ),
        max_length=32
    )
    manage_id = models.CharField(max_length=254, help_text="swarm 就是集群id", blank=True, default="")



class NodeGroupModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.pk}) {self.name}>"