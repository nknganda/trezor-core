# Automatically generated by pb2py
# fmt: off
import protobuf as p


class NEMMosaicSupplyChange(p.MessageType):
    FIELDS = {
        1: ('namespace', p.UnicodeType, 0),
        2: ('mosaic', p.UnicodeType, 0),
        3: ('type', p.UVarintType, 0),
        4: ('delta', p.UVarintType, 0),
    }

    def __init__(
        self,
        namespace: str = None,
        mosaic: str = None,
        type: int = None,
        delta: int = None,
    ) -> None:
        self.namespace = namespace
        self.mosaic = mosaic
        self.type = type
        self.delta = delta
