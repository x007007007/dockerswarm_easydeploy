from django.contrib import admin

from ..models import StackConfigModel, ServiceConfigModel
from ..action import deploy_stack


class SelectServiceConfigInline(admin.TabularInline):
    model = ServiceConfigModel


@admin.register(StackConfigModel)
class StackConfigModelAdmin(admin.ModelAdmin):
    list_filter = (
    )
    list_display = (
        'pk',
        'name',
        'domain_name',
    )
    inlines = [
        SelectServiceConfigInline
    ]

    actions = [
        'action_deploy'
    ]

    def action_deploy(self, request, queryset):
        for obj in queryset:
            assert isinstance(obj, StackConfigModel), f"{obj}"
            deployer = deploy_stack.DeployStackAction(obj)
            deployer.send_query()
