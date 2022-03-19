from django.contrib import admin

from ..models import ServiceConfigModel, ServiceExportPolicyModel, ServiceEnvConfigModel


class ServiceExportPolicyInlineAdmin(admin.TabularInline):
    max_num = 1
    min_num = 0
    model = ServiceExportPolicyModel


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
