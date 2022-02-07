from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dockerswarm_easydeploy.apps.core'
    label = 'docker_swarm_ez_core'
