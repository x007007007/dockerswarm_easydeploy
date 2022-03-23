from django.db import models


class NetworkModel(models.Model):
    TYPE_BRIDGE = 'bridge'
    TYPE_OVERLAY = 'overlay'
    # https://docs.docker.com/network/overlay/
    TYPE_IPVLAN = 'ipvlan'
    TYPE_MACVLAN = 'macvlan'

    name = models.CharField(max_length=64)
    net_addr = models.CharField(max_length=128, blank=True, default='')

    type = models.CharField(choices=(
        (TYPE_BRIDGE, TYPE_BRIDGE),
        (TYPE_OVERLAY, TYPE_OVERLAY),
        (TYPE_IPVLAN, TYPE_IPVLAN),
        (TYPE_MACVLAN, TYPE_MACVLAN),
    ), max_length=32)

    enable_ipv6 = models.BooleanField(default=False)
    enable_encrypted = models.BooleanField(default=False, help_text='用于overlay模式, linux only')
    attachable = models.BooleanField(default=False, help_text='')

    def __str__(self):
        return f"<{self.__class__.__name__}({self.id}) {self.type} {self.name}>"
