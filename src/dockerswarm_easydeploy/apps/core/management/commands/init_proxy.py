import os.path

from django.core.management import BaseCommand
import grpc
from dockerswarm_easydeploy_proto import client_pb2 as pb2, \
    client_pb2_grpc as pb2_grpc

from dockerswarm_easydeploy.apps.core.action.deploy_dependence import DeployDependenceAction


class Command(BaseCommand):

    def handle(self, *args, **options):
        deploy_dep = DeployDependenceAction()
        deploy_dep.send_query('localhost:15005')