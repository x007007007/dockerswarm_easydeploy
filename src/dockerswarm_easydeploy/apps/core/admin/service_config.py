from django.contrib import admin

from ..models import ServiceConfigModel, ServiceDeployPolicyModel, ServiceExportPolicyItemModel, ServiceExportPolicyModel


class ServiceExportPolicyInlineAdmin(admin.TabularInline):
    max_num = 1
    min_num = 0
    model = ServiceExportPolicyModel


@admin.register(ServiceConfigModel)
class ServiceConfigModelAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "stack",
        "host_name",
        "image",
        "deploy_policy",
    )

    inlines = [
        ServiceExportPolicyInlineAdmin,
    ]
