from django.contrib import admin

from ..models import ServiceConfigModel, ServiceDeployPolicyModel, ServiceExportPolicyItemModel, ServiceExportPolicyModel


class ServiceExportPolicyItemModelInlineAdmin(admin.TabularInline):
    model = ServiceExportPolicyItemModel


@admin.register(ServiceExportPolicyModel)
class ServiceExportPolicyModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'only_apply_for_service',
        'only_apply_for_stack',
    )
    inlines = [ServiceExportPolicyItemModelInlineAdmin]