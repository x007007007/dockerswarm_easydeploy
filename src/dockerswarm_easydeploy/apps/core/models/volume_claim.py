from django.db import models


class VolumeClaimModel(models.Model):
    name = models.CharField(max_length=64)
    image_serial = models.ForeignKey("ImageSerialNodel", on_delete=models.CASCADE)

    enable_instance_migration = models.BooleanField(default=True)
    type = models.CharField(max_length=16, choices=(
        ("volume", "volume"),
        ("bind", "bind"),
        ("tmp", "tmp"),
    ))
    src = models.CharField(max_length=254, help_text="相对路径", blank=True, default="")
    dst = models.CharField(max_length=254)

    is_readonly = models.BooleanField(default=False)


    class Meta:
        unique_together = (
            ('name', 'image_serial'),
        )