from django.contrib import admin

from ..models import ExportConfigModel


@admin.register(ExportConfigModel)
class ExportConfigModelAdmin(admin.ModelAdmin):

    list_display = (
        
    )
