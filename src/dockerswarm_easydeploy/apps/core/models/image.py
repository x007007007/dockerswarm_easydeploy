import typing

from django.db import models


class ImageSerialNodel(models.Model):
    name = models.CharField(max_length=254, blank=True, default="")

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id}) {self.name}>"

    def get_image_url(self):
        return self.name


class ImageQuerySet(models.QuerySet):
    pass


class ImageModel(models.Model):
    name = models.ForeignKey("ImageSerialNodel", on_delete=models.CASCADE)
    hash = models.CharField(max_length=254)
    entrypoint = models.JSONField()
    cmds = models.JSONField(null=True)
    user = models.CharField(max_length=254, default='root', blank=True)
    work_dir = models.CharField(max_length=254, default='', blank=True)
    history = models.TextField(blank=True)

    def update_env_list(self, env_map: typing.Dict[str, str]):
        l = self.imageenvmodel_set.values_list('key', 'value')
        db_list = set((i[0], i[1]) for i in l)
        new_list = set((k, v) for k, v in env_map.items())
        self.imageenvmodel_set.filter(key__in=(item[0] for item in db_list - new_list)).delete()
        for obj in ImageEnvModel.objects.bulk_create([
            ImageEnvModel(
                key=item[0],
                value=item[1],
                image=self,
            ) for item in new_list - db_list
        ]):
            self.imageenvmodel_set.add(obj, bulk=False)

    def update_label_list(self, label_map: typing.Dict[str, str]):
        l = self.imageenvmodel_set.values_list('key', 'value')
        db_list = set((i[0], i[1]) for i in l)
        new_list = set((k, v) for k, v in label_map.items())
        self.imagelabelmodel_set.filter(key__in=(item[0] for item in db_list - new_list)).delete()
        for obj in ImageLabel.objects.bulk_create([
            ImageLabel(
                key=item[0],
                value=item[1],
                image=self,
            ) for item in new_list - db_list
        ]):
            self.imagelabelmodel_set.add(obj, bulk=False)


class ImageLabelModel(models.Model):
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