from django.db import models


class ExportConfigModel(models.Model):
    domain_FQAN = models.CharField(max_length=254)