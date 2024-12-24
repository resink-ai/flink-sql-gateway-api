from enum import Enum


class RowFormat(str, Enum):
    JSON = "JSON"
    PLAIN_TEXT = "PLAIN_TEXT"

    def __str__(self) -> str:
        return str(self.value)
