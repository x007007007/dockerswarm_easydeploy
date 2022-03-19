from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey


class EnvNodeModel(MPTTModel):
    name = models.CharField(max_length=254)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return f"<{self.__class__.__name__}: ({self.pk}) {self.name}>"


class EvnItemModel(models.Model):
    is_security = models.BooleanField(default=False)
    default_key = models.CharField(max_length=254)
    value = models.CharField(max_length=254)
    node = models.ForeignKey("EnvNodeModel", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"<{self.__class__.__name__}: ({self.pk}) {self.default_key}>"