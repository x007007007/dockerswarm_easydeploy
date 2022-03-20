from dockerswarm_easydeploy_proto import client_pb2 as pb2, \
    client_pb2_grpc as pb2_grpc
import os
import grpc
import typing
from concurrent import futures
import requests
import docker
from docker.models.services import Service as DockerService
from loguru import logger
import time
import socket
import functools
from dockerswarm_easydeploy_client.pb_json_encoder import pb_decode


def capture_error(fun):
    @functools.wraps(fun)
    def warper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except:
            logger.exception(f"{fun} failed")
    return warper


class DockerSwarmEasyDeployClientService(pb2_grpc.DeployClientServicer):
    __docker_client: typing.Optional[docker.DockerClient] = None

    def __init__(self, volume_map_path=None):
        if volume_map_path is None:
            volume_map_path = "/data"
        self.volume_map_path = volume_map_path

    def pb_decode(self, obj):
        return pb_decode(obj)

    def get_docker_client(self) -> docker.DockerClient:
        if self.__docker_client:
            return self.__docker_client
        try:
            docker_client = docker.from_env()
        except Exception as e:
            logger.exception("from env failed")
            docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        self.__docker_client = docker_client
        logger.debug(f"get_docker_client: {docker_client}")
        return docker_client

    def upload_file(self, request_iterator: typing.Iterator[pb2.ManagedFile], context):
        """客户端通信给服务端，通信方式可以随意选择，这里我选择第4种通信方式
        """
        for mf in request_iterator:
            logger.debug(f"save file: {mf.rel_path}")
            output_path = os.path.join(self.volume_map_path, mf.rel_path)
            output_folder = os.path.dirname(output_path)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            with open(output_path, 'wb') as fp:
                fp.write(mf.data)
            yield pb2.Result(status=0)
        context.set_code(grpc.StatusCode.OK)

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.OK)
        return pb2.Result(
            status=0
        )

    def info(self, request, context):
        # c = self.get_docker_client()
        # info = c.info()
        context.set_code(grpc.StatusCode.OK)
        return pb2.ClientInfo(
            machine_uuid=Register.get_machine_uuid(),
            hostname=Register.get_host_name(),
        )

    def delete_service(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.OK)
        context.set_details('Method not implemented!')

    def get_service_by_name(self, name) -> DockerService:
        c = self.get_docker_client()
        for service in c.services.list():
            if service.name == name:
                return service

    def check_network(self, container_config: pb2.BasicContainerRunConfig):
        c = self.get_docker_client()
        network_map = {n.name: n for n in c.networks.list()}
        for network in container_config.networks:
            if network not in network_map:
                logger.error(f"network `{network}` not exist")
                return False


    @capture_error
    def update_service(self, request_iterator: typing.Iterator[pb2.ServiceConfig], context):
        c = self.get_docker_client()
        for item in request_iterator:
            if self.check_network(item.container):
                yield pb2.Result(
                    status=1,
                )
                continue
            kwargs = dict(
                image=item.container.image,
                command=list(item.container.entrypoints),
                args=list(item.container.cmds),
                name=item.name,
                env=item.container.envs,
            )
            kwargs = self.pb_decode(kwargs)
            logger.debug(f"docker config: {kwargs}")
            if service := self.get_service_by_name(item.name):
                logger.debug(f"update docker service `{item.name}` `{service.id}`")
                service.update(
                    **kwargs
                )
            else:
                logger.debug(f"create docker service `{item.name}`")
                service = c.services.create(**kwargs)
                logger.debug(f"{service}")
            yield pb2.Result(
                status=0,
                resource=pb2.DockerResourceUUID(
                    uuid=service.id
                )
            )
        context.set_code(grpc.StatusCode.OK)
        # context.set_details('run finish')

    # def create_container(self, request_iterator, context):
    #     """Missing associated documentation comment in .proto file."""
    #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    #     context.set_details('Method not implemented!')
    #     raise NotImplementedError('Method not implemented!')
    #
    # def update_container(self, request_iterator, context):
    #     """Missing associated documentation comment in .proto file."""
    #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    #     context.set_details('Method not implemented!')
    #     raise NotImplementedError('Method not implemented!')

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

    def create_network(self, request_iterator: typing.Iterator[pb2.NetworkConfig], context):
        """
        """
        c = self.get_docker_client()
        for nw_pb in request_iterator:
            nw_kwargs = dict(
                name=nw_pb.name,
                options=nw_pb.options,
                driver=nw_pb.driver,
                internal=nw_pb.internal or False,
                labels=nw_pb.labels or None,
                enable_ipv6=nw_pb.enable_ipv6 or False,
                attachable=nw_pb.attachable or False,
                scope=nw_pb.scope,
                ingress=nw_pb.ingress,
            )
            if nw_pb.ipam: nw_kwargs['ipam'] = nw_pb.ipam
            nw_kwargs = self.pb_decode(nw_kwargs)
            logger.debug(f"network create args: {nw_kwargs}")
            res = c.networks.create(**nw_kwargs)
            yield pb2.Result(
                status=0,
                resource=pb2.DockerResourceUUID(
                    uuid=res.id,
                )
            )
        context.set_code(grpc.StatusCode.OK)
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
                time.sleep(600)


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
