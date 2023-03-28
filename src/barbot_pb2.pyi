from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FlavorReply(_message.Message):
    __slots__ = ["flavor_name", "user_id"]
    FLAVOR_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    flavor_name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., flavor_name: _Optional[str] = ...) -> None: ...

class FlavorRequest(_message.Message):
    __slots__ = ["flavor_id", "flavor_name", "user_id"]
    FLAVOR_ID_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    flavor_id: int
    flavor_name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., flavor_name: _Optional[str] = ..., flavor_id: _Optional[int] = ...) -> None: ...

class LevelReply(_message.Message):
    __slots__ = ["container_id", "container_level"]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    container_id: int
    container_level: float
    def __init__(self, container_id: _Optional[int] = ..., container_level: _Optional[float] = ...) -> None: ...

class LevelRequest(_message.Message):
    __slots__ = ["container_id"]
    CONTAINER_ID_FIELD_NUMBER: _ClassVar[int]
    container_id: int
    def __init__(self, container_id: _Optional[int] = ...) -> None: ...

class OrderReply(_message.Message):
    __slots__ = ["drink_name", "user_id"]
    DRINK_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    drink_name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., drink_name: _Optional[str] = ...) -> None: ...

class OrderRequest(_message.Message):
    __slots__ = ["amount_oz", "container_num", "drink_name", "stirring", "user_id"]
    AMOUNT_OZ_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NUM_FIELD_NUMBER: _ClassVar[int]
    DRINK_NAME_FIELD_NUMBER: _ClassVar[int]
    STIRRING_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    amount_oz: float
    container_num: int
    drink_name: str
    stirring: bool
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., drink_name: _Optional[str] = ..., container_num: _Optional[int] = ..., amount_oz: _Optional[float] = ..., stirring: bool = ...) -> None: ...
