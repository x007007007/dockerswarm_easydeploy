from django.contrib import admin
from django.contrib import messages

from ..models import NodeModel
from ..action.docker_image_info import ReadDockerImageAction


@admin.register(NodeModel)
class NodeModelAdmin(admin.ModelAdmin):
    list_filter = (
        'last_update_time',
        'group',
    )
    list_display = (
        'pk',
        'display_name',
        'uuid',
        'machine_id',
        'group',
        'client_port',
        'client_addr',
        'last_update_time',
        'created_time',
        'is_enable',
        'is_delete',
        'is_swarm_node',
        'is_swarm_manager',
    )

    def get_queryset(self, request):
        return NodeModel.objects.select_related('group').all()

    def action_update_node_image_info(self, request, queryset):
        for obj in queryset:
            assert isinstance(obj, NodeModel)
            action = ReadDockerImageAction(node=obj)
            for image_with_status in action.iter_send_query():
                if image_with_status[1]:
                    messages.add_message(request, level=messages.SUCCESS, message=f"find new image: {image_with_status[0]}")
    actions = [
        'action_update_node_image_info',
    ]