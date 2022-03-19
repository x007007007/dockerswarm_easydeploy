from django.core.management import CommandError, BaseCommand
from dockerswarm_easydeploy.apps.core.models import (
    ExportConfigModel,
)
import grpc
import docker_swarm_easy_deploy_proto_pb2 as pb2
import docker_swarm_easy_deploy_proto_pb2_grpc as pb2_grpc

class Command(BaseCommand):

    def data_make(self):
        for i in range(10):
            yield

    def handle(self, *args, **options):
        channel = grpc.insecure_channel('localhost:15005')
        client = pb2_grpc.DeployClientStub(channel)
        res = client.upload_file(iter([pb2.ManagedFile(
                rel_path="test",
                data=b'sss'
            )]))

        for i in res:
            print(i)
