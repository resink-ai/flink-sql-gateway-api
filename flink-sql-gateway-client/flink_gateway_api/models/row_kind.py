from enum import Enum


class RowKind(str, Enum):
    DELETE = "DELETE"
    INSERT = "INSERT"
    UPDATE_AFTER = "UPDATE_AFTER"
    UPDATE_BEFORE = "UPDATE_BEFORE"

    def __str__(self) -> str:
        return str(self.value)
