from django.db import models

# Create your models here.


class StackConfigQueryset(models.QuerySet):

    def inner(self):
        return self.filter(
            is_inner=True
        )

    def user_config(self):
        return self.filter(
            is_inner=False
        )


class StackConfigModel(models.Model):
    """
    一组服务
    """
    objects = StackConfigQueryset.as_manager()

    name = models.CharField(max_length=100, unique=True)
    is_inner = models.BooleanField(default=False)
    domain_name = models.CharField(max_length=254, help_text="一个域，其他服务部署在这个域中")


    def __str__(self):
        return f"<{self.__class__.__name__} ({self.pk}) {self.name} domain:{self.domain_name}>"