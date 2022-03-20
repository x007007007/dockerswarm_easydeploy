from django.contrib import admin

from ..models import ServiceConfigModel


class ServiceExportPolicyInlineAdmin(admin.TabularInline):
    model = ServiceConfigModel.port_set.through
    readonly_fields = (
        "is_image_cnf",
    )
    fields = (
        "id",
        "inner_port",
        "export_policy",
        "is_image_cnf",
    )

class EnvConfigInlineAdmin(admin.TabularInline):
    model = ServiceConfigModel.env_set.through

    readonly_fields = (
        'real_value',
    )
    fields = (
        'env_item',
        'value',
        'key',
        'real_value',
    )


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
        EnvConfigInlineAdmin,
        ServiceExportPolicyInlineAdmin,
    ]
