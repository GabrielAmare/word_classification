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
    pass


@dataclasses.dataclass(frozen=True)
class InterjectionOnomatopoeic(Interjection):
    pass


@dataclasses.dataclass(frozen=True)
class InterjectionBorrowed(Interjection):
    pass
