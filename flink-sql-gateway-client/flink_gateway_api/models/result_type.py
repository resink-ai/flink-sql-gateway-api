from enum import Enum


class ResultType(str, Enum):
    EOS = "EOS"
    NOT_READY = "NOT_READY"
    PAYLOAD = "PAYLOAD"

    def __str__(self) -> str:
        return str(self.value)
