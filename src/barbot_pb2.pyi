from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CleanReply(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CleanRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class OrderReply(_message.Message):
    __slots__ = ["drink_name", "flavor_name", "user_id"]
    DRINK_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    drink_name: str
    flavor_name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., drink_name: _Optional[str] = ..., flavor_name: _Optional[str] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = ["container_amounts", "drink_name", "flavor_id", "flavor_name", "user_id"]
    CONTAINER_AMOUNTS_FIELD_NUMBER: _ClassVar[int]
    DRINK_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    container_amounts: _containers.RepeatedCompositeFieldContainer[OrderTuple]
    drink_name: str
    flavor_id: int
    flavor_name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., drink_name: _Optional[str] = ..., container_amounts: _Optional[_Iterable[_Union[OrderTuple, _Mapping]]] = ..., flavor_name: _Optional[str] = ..., flavor_id: _Optional[int] = ...) -> None: ...

class OrderTuple(_message.Message):
    __slots__ = ["amount_oz", "container_id"]
    AMOUNT_OZ_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    amount_oz: float
    container_id: int
    def __init__(self, container_id: _Optional[int] = ..., amount_oz: _Optional[float] = ...) -> None: ...
