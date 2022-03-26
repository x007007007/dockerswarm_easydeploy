from django.contrib import admin

from ..models import VolumeClaimModel


@admin.register(VolumeClaimModel)
class VolumeClaimModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image_serial",
        "enable_instance_migration",
        "type",
        "src",
        "dst",
        "is_readonly",
    )
