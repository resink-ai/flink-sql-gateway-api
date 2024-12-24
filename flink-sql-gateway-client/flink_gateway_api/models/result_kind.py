from enum import Enum


class ResultKind(str, Enum):
    SUCCESS = "SUCCESS"
    SUCCESS_WITH_CONTENT = "SUCCESS_WITH_CONTENT"

    def __str__(self) -> str:
        return str(self.value)
