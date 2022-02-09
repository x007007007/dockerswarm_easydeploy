from django.db import models


class ServiceExportPolicyItemModel(models.Model):
    policy = models.ForeignKey("ServiceExportPolicyModel", on_delete=models.CASCADE)
    protocol = models.CharField(
        max_length=6,
        choices=(
            ("udp", "udp"),
            ("tcp", "tcp"),
            ("http", "http"),
            ("https", "https"),
        ),
    )
    is_force_https = models.BooleanField(default=True)
    sni_name = models.CharField(max_length=100, help_text="http/https only", default="", blank=True)
    port = models.IntegerField(default=-1, help_text="udp/tcp only")
    inner_port = models.IntegerField(default=-1)
