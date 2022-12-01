import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Number, Gender

__all__ = [
    'Noun',
    'NounCommon',
    'NounProper',
]


@dataclasses.dataclass(frozen=True)
class Noun(Meaning, abc.ABC):
    number: Number
    gender: Gender


@dataclasses.dataclass(frozen=True)
class NounCommon(Noun):
    def __str__(self) -> str:
        return f"NOM-COM-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class NounProper(Noun):
    def __str__(self) -> str:
        return f"NOM-PRO-{self.number.value}{self.gender.value}"
