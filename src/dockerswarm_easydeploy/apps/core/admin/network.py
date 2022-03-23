from ..models import NetworkModel
from django.contrib import admin


@admin.register(NetworkModel)
class NetworkModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'net_addr',
        'attachable',
        'enable_ipv6',
        'enable_encrypted'
    )