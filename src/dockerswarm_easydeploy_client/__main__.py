from .service import serve


def main():
    hub_host = os.environ.get("DOCKERSWARM_EASYDEPLOY_HUB", "dockerswarm-easydeploy")
    ip = os.environ.get("DOCKERSWARM_EASYDEPLOY_CLIENT_LISTEN_IP", "0.0.0.0")
    port = os.environ.get("DOCKERSWARM_EASYDEPLOY_CLIENT_LISTEN_PORT", "15005")
    serve(hub_host, address=ip, port=port)


if __name__ == '__main__':
    main()