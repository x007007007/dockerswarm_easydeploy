import docker_swarm_easy_deploy_proto_pb2_grpc as pb2_grpc
import docker_swarm_easy_deploy_proto_pb2 as pb2
import os
import grpc
import typing
from concurrent import futures
import requests
import docker
from loguru import logger
import time
import socket


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


class Register:
    def __init__(self, service_host, listen_port=15005):
        self.listen_port = listen_port
        self.service_host = service_host

    @staticmethod
    def get_machine_uuid():
        for f in ['/sys/class/dmi/id/board_serial', '/host/sys/class/dmi/id/board_serial']:
            if os.path.exists(f):
                with open("/sys/class/dmi/id/board_serial") as fp:
                    return fp.read()
        return ''

    @staticmethod
    def get_docker_info():
        try:
            docker_client = docker.from_env()
        except Exception as e:
            logger.exception("from env failed")
            docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        return docker_client.info()

    def get_host_name(self):
        return socket.getfqdn()

    def post_info(self):
        req_data = dict(
            machine_id=self.get_machine_uuid(),
            docker_info=self.get_docker_info(),
            client_addr=self.get_host_name(),
            client_port=self.listen_port
        )
        logger.debug(f"post: {req_data}")
        res = requests.post(f"{self.service_host}/api/v1/node/register/", json=req_data)
        resp = res.json()
        logger.debug(f"{resp}")

    def start(self):
        while True:
            try:
                self.post_info()
            except:
                logger.exception("update status failed")
            finally:
                time.sleep(5)


def serve(hub_host, address=None, port=15005):
    if address is None:
        address = '0.0.0.0'
    local_listen = f"{address}:{port}"
    logger.level("DEBUG")
    # gRPC 服务器
    thread_pool = futures.ThreadPoolExecutor(max_workers=10)
    server = grpc.server(thread_pool)
    pb2_grpc.add_DeployClientServicer_to_server(DockerSwarmEasyDeployClientService(
        volume_map_path="/Users/xxc/workspace/github.com/x007007007/docker_swarm_easy_deploy/output"
    ), server)
    register = Register(service_host=hub_host)
    register_handle = thread_pool.submit(register.start)
    register_handle.add_done_callback(server.stop)
    server.add_insecure_port(local_listen)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve(hub_host='http://127.0.0.1:8000')
