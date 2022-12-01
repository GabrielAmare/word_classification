import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Person, Number, Gender

__all__ = [
    'Pronoun',
    'PronounPersonal',
    'PronounAdverbial',
    'PronounRelative',
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
    """
        Example :
        >>> from semantic.entities import Person, Number, Gender
        >>> _ = PronounPersonal(person=Person.FIRST, number=Number.SINGULAR, gender=Gender.ANY)  # je
        >>> _ = PronounPersonal(person=Person.SECOND, number=Number.SINGULAR, gender=Gender.ANY)  # tu
        >>> _ = PronounPersonal(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE)  # il
        >>> _ = PronounPersonal(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE)  # elle
        >>> _ = PronounPersonal(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.ANY)  # on
        >>> _ = PronounPersonal(person=Person.FIRST, number=Number.PLURAL, gender=Gender.ANY)  # nous
        >>> _ = PronounPersonal(person=Person.SECOND, number=Number.PLURAL, gender=Gender.ANY)  # vous
        >>> _ = PronounPersonal(person=Person.THIRD, number=Number.PLURAL, gender=Gender.MALE)  # ils
        >>> _ = PronounPersonal(person=Person.THIRD, number=Number.PLURAL, gender=Gender.FEMALE)  # elles
    """
    person: Person
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-PER-{self.person.value}{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounAdverbial(Pronoun):
    """
        Example :
        >>> _ = PronounAdverbial()  # y, en
    """
    
    def __str__(self) -> str:
        return "PRO-ADV"


@dataclasses.dataclass(frozen=True)
class PronounRelative(Pronoun, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class PronounRelativeInvariable(PronounRelative):
    """
        Example :
        >>> _ = PronounRelativeInvariable()  # qui, que, quoi, dont, où
    """
    
    def __str__(self) -> str:
        return "PRO-REL"


@dataclasses.dataclass(frozen=True)
class PronounRelativeVariable(PronounRelative):
    """
        Example :
        >>> from semantic.entities import Person, Number, Gender
        >>> _ = PronounRelativeVariable(person=Person.FIRST, number=Number.SINGULAR, gender=Gender.MALE)  # lequel
        >>> _ = PronounRelativeVariable(person=Person.FIRST, number=Number.SINGULAR, gender=Gender.FEMALE)  # laquelle
        >>> _ = PronounRelativeVariable(person=Person.FIRST, number=Number.PLURAL, gender=Gender.MALE)  # lequels
        >>> _ = PronounRelativeVariable(person=Person.FIRST, number=Number.PLURAL, gender=Gender.FEMALE)  # lesquelles
    """
    person: Person
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-REL-{self.person.value}{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounInterrogative(Pronoun):
    """
        Example :
        >>> _ = PronounInterrogative()  # qui, que, quoi
    """
    
    def __str__(self) -> str:
        return f"PRO-INT"


@dataclasses.dataclass(frozen=True)
class PronounPossessive(Pronoun):
    owner_person: Person
    owner_number: Number
    owned_number: Number
    owned_gender: Gender
    
    def __str__(self) -> str:
        return "-".join((
            "PRO",
            "POS",
            f"{self.owner_person.value}{self.owned_number.value}",
            f"{self.owned_number.value}{self.owned_gender}"
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
    person: Person
    number: Number
    gender: Gender
    
    def __str__(self) -> str:
        return f"PRO-IMP-{self.person.value}{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class PronounReflexive(Pronoun):
    person: Person
    number: Number
    
    def __str__(self) -> str:
        return f"PRO-REF-{self.person.value}{self.number.value}"
