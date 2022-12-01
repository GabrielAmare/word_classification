import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Person, Number, Gender

__all__ = [
    'Adjective',
    'AdjectiveQualifying',
    'AdjectiveRelative',
    'AdjectiveIndefinite',
    'AdjectiveNumeral',
    'AdjectiveNumeralCardinal',
    'AdjectiveNumeralOrdinal',
    'AdjectivePossessive',
]


@dataclasses.dataclass(frozen=True)
class Adjective(Meaning, abc.ABC):
    number: Number
    gender: Gender


@dataclasses.dataclass(frozen=True)
class AdjectiveQualifying(Adjective):
    def __str__(self) -> str:
        return f"ADJ-QUA-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class AdjectiveRelative(Adjective):
    def __str__(self) -> str:
        return f"ADJ-REL-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class AdjectiveIndefinite(Adjective):
    def __str__(self) -> str:
        return f"ADJ-IND-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class AdjectiveNumeral(Adjective, abc.ABC):
    value: int


@dataclasses.dataclass(frozen=True)
class AdjectiveNumeralCardinal(AdjectiveNumeral):
    def __str__(self) -> str:
        return f"ADJ-NUM-{self.number.value}{self.gender.value}-CAR-{self.value!s}"


@dataclasses.dataclass(frozen=True)
class AdjectiveNumeralOrdinal(AdjectiveNumeral):
    def __str__(self) -> str:
        return f"ADJ-NUM-{self.number.value}{self.gender.value}-ORD-{self.value!s}"


@dataclasses.dataclass(frozen=True)
class AdjectivePossessive(Adjective):
    owner_person: Person
    owner_number: Number
    tonic: bool
    
    def __str__(self) -> str:
        return "-".join((
            f"ADJ-POS-{self.number.value}{self.gender.value}",
            f"{self.owner_person.value}{self.owner_number.value}",
            "T" if self.tonic else "N",
        ))
