from django.db import models

# Create your models here.


class StackConfigModel(models.Model):
    """
    一组服务
    """
    name = models.CharField(max_length=100, unique=True)
    domain_name = models.CharField(max_length=254, help_text="一个域，其他服务部署在这个域中")


    def __str__(self):
        return f"<{self.__class__.__name__} ({self.pk}) {self.name} domain:{self.domain_name}>"