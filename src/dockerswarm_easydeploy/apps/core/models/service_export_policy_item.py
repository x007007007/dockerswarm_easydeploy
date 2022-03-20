from django.db import models


class ServiceExportPolicyItemModel(models.Model):
    """
    服务端口怎么暴露到域中,
    部署时决定
    """
    TYPE_TCP = 'tcp'
    TYPE_UDP = 'udp'
    TYPE_TCP_UDP = 'tcp/udp'
    TYPE_ONLY_HTTP = 'http'
    TYPE_ONLY_HTTPS = 'https'
    TYPE_HTTP1_1 = 'http(s)'
    protocol = models.CharField(
        max_length=8,
        choices=(
            (TYPE_UDP, TYPE_UDP),
            (TYPE_TCP, TYPE_TCP),
            (TYPE_TCP_UDP, TYPE_TCP_UDP),
            (TYPE_ONLY_HTTP, TYPE_ONLY_HTTP),
            (TYPE_ONLY_HTTPS, TYPE_ONLY_HTTPS),
        ),
    )
    is_force_https = models.BooleanField(default=True)
    sni_name = models.CharField(max_length=100, help_text="http/https only", default="", blank=True)
    port = models.IntegerField(default=-1, help_text="udp/tcp only")

    def __str__(self):
        if self.protocol in (self.TYPE_UDP, self.TYPE_TCP, self.TYPE_TCP_UDP):
            return f"<export:{self.port}/{self.protocol}>"
        else:
            return f"<export:{self.protocol}://{self.sni_name}>"
