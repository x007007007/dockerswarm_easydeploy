from django.contrib import admin
from django.urls import path, re_path, include

import dockerswarm_easydeploy.apps.core.apps

from dockerswarm_easydeploy.apps.core import api

urlpatterns = [
    path("node/register/", api.node.register.RegisterNodeCreateOrUpdateView.as_view())
]