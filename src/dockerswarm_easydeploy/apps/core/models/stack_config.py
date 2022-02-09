from django.db import models

# Create your models here.


class StackConfigModel(models.Model):
    name = models.CharField(max_length=100)


