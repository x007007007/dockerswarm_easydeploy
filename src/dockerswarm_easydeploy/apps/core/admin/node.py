from django.contrib import admin

from ..models import NodeModel


@admin.register(NodeModel)
class NodeModelAdmin(admin.ModelAdmin):
    list_filter = (
        'last_update_time',
        'group',
    )
    list_display = (
        'pk',
        'uuid',
        'machine_id',
        'group',
        'client_port',
        'client_addr',
        'last_update_time',
        'created_time',
    )

    def get_queryset(self, request):
        return NodeModel.objects.select_related('group').all()