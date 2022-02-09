from django.contrib import admin

from ..models import ServiceDeployPolicyModel


@admin.register(ServiceDeployPolicyModel)
class ServiceDeployPolicyModelAdmin(admin.ModelAdmin):
    list_display = (
        "is_manager_only",
        "is_work_only",
        "is_privilege",
    )
