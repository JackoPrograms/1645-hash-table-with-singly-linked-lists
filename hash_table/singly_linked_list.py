from typing import Generic, Optional, TypeVar

KT = TypeVar('KT')
VT = TypeVar('VT')


class SinglyLinkedList(Generic[KT, VT]):
    def __init__(
        self,
        key: KT,
        value: VT,
        next_node: Optional['SinglyLinkedList[KT, VT]'] = None,
    ) -> None: ...
