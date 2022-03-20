import json
import typing

from google.protobuf.pyext._message import RepeatedScalarContainer, ScalarMapContainer


class ProtobufJsonEncoder(json.JSONEncoder):
    def default(self, o: typing.Any) -> typing.Any:
        if isinstance(o, RepeatedScalarContainer):
            return list(o)
        return super(ProtobufJsonEncoder, self).default(o)


def pb_decode(obj):
    if isinstance(obj, (list, RepeatedScalarContainer)):
        return [
            pb_decode(i) for i in obj
        ]
    elif isinstance(obj, (dict, ScalarMapContainer,)):
        return {
            k: pb_decode(v)
            for k, v in obj.items()
        }
    return obj