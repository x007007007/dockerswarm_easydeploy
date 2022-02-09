from django.db import models


class ImageModel(models.Model):
    name = models.CharField(max_length=254)


class ImageExportModel(models.Model):
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    port = models.IntegerField()