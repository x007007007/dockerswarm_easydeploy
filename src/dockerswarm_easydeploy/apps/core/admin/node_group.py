from django.contrib import admin

from ..models import NodeGroupModel


@admin.register(NodeGroupModel)
class NodeGroupModelAdmin(admin.ModelAdmin):
    list_filter = (
    )
    list_display = (
        'pk',
        'name',
    )

