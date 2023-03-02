from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrderReply(_message.Message):
    __slots__ = ["ack"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: str
    def __init__(self, ack: _Optional[str] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = ["drink_num", "user_id"]
    DRINK_NUM_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    drink_num: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., drink_num: _Optional[int] = ...) -> None: ...
