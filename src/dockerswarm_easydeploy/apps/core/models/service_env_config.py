from django.db import models


class ServiceEnvConfigModel(models.Model):
    """
    跟着image走
    """
    env_item = models.ForeignKey("EvnItemModel", on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=254, null=True, blank=True, help_text="值")
    key = models.CharField(max_length=254, null=True, blank=True, help_text="使用新的名称")
    service = models.ForeignKey("ServiceConfigModel", on_delete=models.CASCADE)

    @property
    def real_value(self):
        if self.env_item:
            return self.env_item.value
        return self.env_item.value
