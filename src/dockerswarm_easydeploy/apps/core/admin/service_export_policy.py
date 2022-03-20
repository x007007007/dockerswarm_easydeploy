from django.contrib import admin

from ..models import ServicePortConfigModel, ServiceExportPolicyItemModel


@admin.register(ServicePortConfigModel)
class ServicePortConfigModelAdmin(admin.ModelAdmin):
    list_display = (
        "is_image_cnf",
        "export_policy",
        "service",
        "inner_port",
    )
    
    
@admin.register(ServiceExportPolicyItemModel)
class ServiceExportPolicyItemModelAdmin(admin.ModelAdmin):
    list_display = (
        "protocol",
        "is_force_https",
        "sni_name",
        "port",
    )
