import dataclasses

from ..models import NodeModel


@dataclasses.dataclass
class ReadDockerImageAction:

    node: NodeModel

    def filter_image_list(self):
        pass


