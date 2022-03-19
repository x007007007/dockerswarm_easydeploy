import docker_swarm_easy_deploy_proto_pb2_grpc as pb2_grpc
import docker_swarm_easy_deploy_proto_pb2 as pb2
import os
import grpc
import typing
from concurrent import futures
import docker


class DockerSwarmEasyDeployClientService(pb2_grpc.DeployClientServicer):

    def __init__(self, volume_map_path=None):
        if volume_map_path is None:
            volume_map_path = "/data"
        self.volume_map_path = volume_map_path

    def upload_file(self, request_iterator: typing.Iterator[pb2.ManagedFile], context):
        """客户端通信给服务端，通信方式可以随意选择，这里我选择第4种通信方式
        """
        for mf in request_iterator:
            output_path = os.path.join(self.volume_map_path, mf.ral_path)
            output_folder = os.path.dirname(output_path)
            if not os.path.exists(output_path):
                os.makedirs(output_folder)
            with open(output_path, 'wb') as fp:
                fp.write(mf.data)
            yield pb2.Result(status=0)
        context.set_code(grpc.StatusCode.OK)

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_service(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_service(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_service(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_container(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_container(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_container(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update_node(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_network(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_network(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def serve(address=None):
    if address is None:
        address = '0.0.0.0:15005'
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DeployClientServicer_to_server(DockerSwarmEasyDeployClientService(
        volume_map_path="/Users/xxc/workspace/github.com/x007007007/docker_swarm_easy_deploy/output"
    ), server)
    server.add_insecure_port(address)
    server.start()
    server.wait_for_termination()

