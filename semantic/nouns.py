import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Entity

__all__ = [
    'Noun',
    'CommonNoun',
    'ProperNoun',
]


@dataclasses.dataclass(frozen=True)
class Noun(Meaning, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class CommonNoun(Noun):
    """
        Exemple :
        >>> from semantic.entities import Person, Number, Gender
        >>> _ = CommonNoun(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # chat
        >>> _ = CommonNoun(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.MALE))  # chats
        >>> _ = CommonNoun(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # chatte
        >>> _ = CommonNoun(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.FEMALE))  # chattes
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"NOM-COM-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class ProperNoun(Noun):
    """
        Exemple :
        >>> from semantic.entities import Person, Number, Gender
        >>> _ = ProperNoun(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # Michel
        >>> _ = ProperNoun(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # Michelle
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"NOM-PRO-{self.entity!s}"
