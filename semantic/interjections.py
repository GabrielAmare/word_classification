import abc
import dataclasses

from semantic import Meaning

__all__ = [
    'Interjection',
    'InterjectionStrictSensu',
    'InterjectionOnomatopoeic',
    'InterjectionBorrowed',
]


@dataclasses.dataclass(frozen=True)
class Interjection(Meaning, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class InterjectionStrictSensu(Interjection):
    def __str__(self) -> str:
        return "INT-STR"


@dataclasses.dataclass(frozen=True)
class InterjectionOnomatopoeic(Interjection):
    def __str__(self) -> str:
        return "INT-ONO"


@dataclasses.dataclass(frozen=True)
class InterjectionBorrowed(Interjection):
    def __str__(self) -> str:
        return "INT-EMP"
