import os.path

from django.core.management import BaseCommand
import grpc
from dockerswarm_easydeploy_proto import client_pb2 as pb2, \
    client_pb2_grpc as pb2_grpc


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'node_name', help='node name for update',
        )
        parser.add_argument(
            'src', help='local file or folder',
        )
        parser.add_argument(
            'dest', help='remote path',
        )

    def upload_src(self, src_path, dest_path):
        src_path = os.path.abspath(src_path)
        src_path_len = len(src_path)
        if os.path.isfile(src_path):
            with open(src_path, 'rb') as fp:
                yield pb2.ManagedFile(
                    rel_path=dest_path,
                    data=fp.read()
                )
        elif os.path.isdir(src_path):
            for dirpath, dirnames, filenames in os.walk(src_path):
                dirpath = os.path.abspath(dirpath)
                real_dirpath = dirpath[src_path_len:].lstrip('/')
                for filename in filenames:
                    with open(os.path.join(dirpath, filename), 'rb') as fp:
                        yield pb2.ManagedFile(
                            rel_path=os.path.join(dest_path, real_dirpath, filename),
                            data=fp.read()
                        )

    def handle(self, *args, **options):
        channel = grpc.insecure_channel('localhost:15005')
        client = pb2_grpc.DeployClientStub(channel)
        for res in client.upload_file(self.upload_src(options['src'], options['dest'])):
            print(res.status)


