from enum import Enum


class ConstraintType(str, Enum):
    PRIMARY_KEY = "PRIMARY_KEY"
    UNIQUE_KEY = "UNIQUE_KEY"

    def __str__(self) -> str:
        return str(self.value)
