# Automatically generated by pb2py
# fmt: off
import protobuf as p


class Initialize(p.MessageType):
    MESSAGE_WIRE_TYPE = 0
    FIELDS = {
        1: ('state', p.BytesType, 0),
        2: ('skip_passphrase', p.BoolType, 0),
    }

    def __init__(
        self,
        state: bytes = None,
        skip_passphrase: bool = None,
    ) -> None:
        self.state = state
        self.skip_passphrase = skip_passphrase
