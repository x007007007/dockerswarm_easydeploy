from django.db import models


class ServiceVolumeModel(models.Model):
    service = models.ForeignKey("ServiceConfigModel", on_delete=models.CASCADE)
    volume_claim = models.ForeignKey("VolumeClaimModel", on_delete=models.CASCADE)
    node = models.ForeignKey("NodeModel", on_delete=models.CASCADE)
    index = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (
            ('service', 'volume_claim', 'index'),
        )

    def get_volume_name(self):
        return f"{self.service.stack.name}-{self.service.host_name}-{self.volume_claim.name}-{self.index}"

