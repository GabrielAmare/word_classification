import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Person, Number, Gender

__all__ = [
    'Pronoun',
    'PronounPersonal',
    'PronounAdverbial',
    'PronounRelative',
    'PronounRelativeInvariable',
    'PronounRelativeVariable',
    'PronounInterrogative',
    'PronounPossessive',
    'PronounDemonstrative',
    'PronounIndefinite',
    'PronounImpersonal',
    'PronounReflexive',
]


@dataclasses.dataclass(frozen=True)
class Pronoun(Meaning, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class PronounPersonal(Pronoun):
    person: Person
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-PER-{self.person.value}{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounAdverbial(Pronoun):
    def __str__(self) -> str:
        return "PRO-ADV"


@dataclasses.dataclass(frozen=True)
class PronounRelative(Pronoun, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class PronounRelativeInvariable(PronounRelative):
    def __str__(self) -> str:
        return "PRO-REL-INV"


@dataclasses.dataclass(frozen=True)
class PronounRelativeVariable(PronounRelative):
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-REL-VAR-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounInterrogative(Pronoun):
    def __str__(self) -> str:
        return f"PRO-INT"


@dataclasses.dataclass(frozen=True)
class PronounPossessive(Pronoun):
    number: Number
    gender: Gender
    owner_person: Person
    owner_number: Number
    
    def __str__(self) -> str:
        return "-".join((
            f"PRO-POS-{self.number.value}{self.gender.value}",
            f"{self.owner_person.value}{self.owner_number.value}",
        ))


@dataclasses.dataclass(frozen=True)
class PronounDemonstrative(Pronoun):
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-DEM-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounIndefinite(Pronoun):
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-IND-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounImpersonal(Pronoun):
    def __str__(self) -> str:
        return "PRO-IMP"


@dataclasses.dataclass(frozen=True)
class PronounReflexive(Pronoun):
    person: Person
    number: Number
    
    def __str__(self) -> str:
        return f"PRO-REF-{self.person.value}{self.number.value}"
