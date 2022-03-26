from django.contrib import admin
from ..models import (
    ImageModel,
    ImageEnvModel,
    ImageLabel,
    ImageRepoModel,
    ImageSerialNodel,
    ImageTagModel,
    ImageVolumeModel
)


class ImageEnvModelInlineAdmin(admin.TabularInline):
    model = ImageEnvModel
    readonly_fields = (
        'key',
        'value',
    )
    max_num = 0


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "hash",
        "entrypoint",
        "cmds",
        "user",
        "work_dir",
    )

    inlines = [
        ImageEnvModelInlineAdmin,
    ]