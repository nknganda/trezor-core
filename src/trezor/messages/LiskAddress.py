# Automatically generated by pb2py
# fmt: off
import protobuf as p


class LiskAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 115
    FIELDS = {
        1: ('address', p.UnicodeType, 0),
    }

    def __init__(
        self,
        address: str = None,
    ) -> None:
        self.address = address
