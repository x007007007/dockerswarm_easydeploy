from django.db import models


class ImageSerialNodel(models.Model):
    name = models.CharField(max_length=254, blank=True, default="")


class ImageModel(models.Model):
    name = models.ForeignKey("ImageSerialNodel", on_delete=models.CASCADE)
    hash = models.CharField(max_length=254)
    entrypoint = models.CharField(max_length=254)
    cmds = models.JSONField(null=True)
    user = models.CharField(max_length=254, default='root')
    history = models.TextField(blank=True)


class ImageLabel(models.Model):
    key = models.CharField(max_length=254)
    value = models.CharField(max_length=254, blank=True, null=True)
    image = models.ForeignKey("ImageModel", on_delete=models.CASCADE)


class ImageVolumeModel(models.Model):
    path = models.CharField(max_length=254)
    image = models.ForeignKey("ImageModel", on_delete=models.CASCADE)


class ImageEnvModel(models.Model):
    key = models.CharField(max_length=254)
    value = models.CharField(max_length=254, blank=True, null=True)
    image = models.ForeignKey("ImageModel", on_delete=models.CASCADE)


class ImageRepoModel(models.Model):
    url = models.CharField(max_length=254)


class ImageTagModel(models.Model):
    repo = models.ForeignKey("ImageRepoModel", on_delete=models.CASCADE)
    image = models.ForeignKey("ImageModel", on_delete=models.CASCADE)
    tag = models.CharField(max_length=254)


class ImageExposeModel(models.Model):
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    port = models.IntegerField()
    export_port = models.IntegerField()
    protocol = models.CharField(max_length=16)