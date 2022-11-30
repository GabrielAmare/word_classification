import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Entity, Person, Number, Gender

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
    pass


@dataclasses.dataclass(frozen=True)
class AdjectiveQualifying(Adjective):
    """
    Example :
    >>> from semantic.entities import Person
    >>> _ = AdjectiveQualifying(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # bleu
    >>> _ = AdjectiveQualifying(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # bleue
    >>> _ = AdjectiveQualifying(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.MALE))  # bleus
    >>> _ = AdjectiveQualifying(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.FEMALE))  # bleues
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ADJ-QUA-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class AdjectiveRelative(Adjective):
    """
    Example :
    >>> from semantic.entities import Person
    >>> _ = AdjectiveRelative(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # lequel
    >>> _ = AdjectiveRelative(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # laquelle
    >>> _ = AdjectiveRelative(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.MALE))  # lesquels
    >>> _ = AdjectiveRelative(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.FEMALE))  # lesquelles
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ADJ-REL-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class AdjectiveIndefinite(Adjective):
    """
    https://fr.wikipedia.org/wiki/Adjectif_ind%C3%A9fini
    Example :
    >>> from semantic.entities import Person
    >>> _ = AdjectiveIndefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # aucun
    >>> _ = AdjectiveIndefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # aucune
    >>> _ = AdjectiveIndefinite(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.MALE))  # auncuns
    >>> _ = AdjectiveIndefinite(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.FEMALE))  # aucunes
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ADJ-IND-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class AdjectiveNumeral(Adjective, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class AdjectiveNumeralCardinal(AdjectiveNumeral):
    """
    Example :
    >>> from semantic.entities import Person
    >>> _ = AdjectiveNumeralCardinal(number=Number.SINGULAR, gender=Gender.MALE, value=1)  # un
    >>> _ = AdjectiveNumeralCardinal(number=Number.SINGULAR, gender=Gender.FEMALE, value=1)  # une
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=3)  # trois
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=10)  # dix
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=20)  # vingt
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=100)  # cent
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=80)  # quatre-vingts
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=300)  # trois cents
    >>> _ = AdjectiveNumeralCardinal(number=Number.PLURAL, gender=Gender.ANY, value=1970)  # mille neuf cent soixante-dix
    """
    number: Number
    gender: Gender
    value: int
    
    def __str__(self) -> str:
        return f"ADJ-NUM-CAR-{self.number.value}{self.gender.value}-{self.value!s}"


@dataclasses.dataclass(frozen=True)
class AdjectiveNumeralOrdinal(AdjectiveNumeral):
    """
    Example :
    >>> from semantic.entities import Person
    >>> _ = AdjectiveNumeralOrdinal(number=Number.SINGULAR, gender=Gender.MALE, value=1)  # premier
    >>> _ = AdjectiveNumeralOrdinal(number=Number.SINGULAR, gender=Gender.FEMALE, value=1)  # première
    >>> _ = AdjectiveNumeralOrdinal(number=Number.PLURAL, gender=Gender.ANY, value=2)  # deuxième
    >>> _ = AdjectiveNumeralOrdinal(number=Number.PLURAL, gender=Gender.ANY, value=11)  # onzième
    >>> _ = AdjectiveNumeralOrdinal(number=Number.PLURAL, gender=Gender.ANY, value=31)  # trente-et-unième
    >>> _ = AdjectiveNumeralOrdinal(number=Number.PLURAL, gender=Gender.ANY, value=33)  # trente-troisième
    """
    number: Number
    gender: Gender
    value: int
    
    def __str__(self) -> str:
        return f"ADJ-NUM-ORD-{self.number.value}{self.gender.value}-{self.value!s}"


@dataclasses.dataclass(frozen=True)
class AdjectivePossessive(Adjective):
    owner_person: Person
    owner_number: Number
    owned_number: Number
    owned_gender: Gender
    tonic: bool
    
    def __str__(self) -> str:
        return "-".join((
            "ADJ",
            "POS",
            "T" if self.tonic else "N",
            f"{self.owner_person.value}{self.owned_number.value}",
            f"{self.owned_number.value}{self.owned_gender}",
        ))
