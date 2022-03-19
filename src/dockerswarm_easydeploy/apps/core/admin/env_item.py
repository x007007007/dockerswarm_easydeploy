from django.contrib import admin
from mptt import admin as mptt_admin
from dockerswarm_easydeploy.apps.core.models.env_item import EvnItemModel, EnvNodeModel


@admin.register(EnvNodeModel)
class EnvTreeModelAdmin(mptt_admin.MPTTModelAdmin):
    pass


@admin.register(EvnItemModel)
class EvnItemModelAdmin(admin.ModelAdmin):
    pass