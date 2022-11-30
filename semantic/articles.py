import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Entity

__all__ = [
    'Article',
    'ArticleDefinite',
    'ArticleIndefinite',
    'ArticlePartitive',
    'ArticleDemonstrative',
    'ArticleDefiniteContracted',
]


@dataclasses.dataclass(frozen=True)
class Article(Meaning, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class ArticleDefinite(Article):
    """
    Example :
    >>> from semantic.entities import Person, Number, Gender
    >>> _ = ArticleDefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # le
    >>> _ = ArticleDefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # la
    >>> _ = ArticleDefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.ANY))  # l'
    >>> _ = ArticleDefinite(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.ANY))  # les
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ART-DEF-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class ArticleIndefinite(Article):
    """
    Example :
    >>> from semantic.entities import Person, Number, Gender
    >>> _ = ArticleIndefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # un
    >>> _ = ArticleIndefinite(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # une
    >>> _ = ArticleIndefinite(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.ANY))  # des
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ART-IND-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class ArticlePartitive(Article):
    """
    Example :
    >>> from semantic.entities import Person, Number, Gender
    >>> _ = ArticlePartitive(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # du
    >>> _ = ArticlePartitive(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # de la
    >>> _ = ArticlePartitive(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.ANY))  # de l'
    >>> _ = ArticlePartitive(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.ANY))  # des
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ART-PAR-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class ArticleDemonstrative(Article):
    """
    Example :
    >>> from semantic.entities import Person, Number, Gender
    >>> _ = ArticleDemonstrative(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # ce
    >>> _ = ArticleDemonstrative(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # cet
    >>> _ = ArticleDemonstrative(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.FEMALE))  # cette
    >>> _ = ArticleDemonstrative(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.ANY))  # ces
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ART-DEM-{self.entity!s}"


@dataclasses.dataclass(frozen=True)
class ArticleDefiniteContracted(Article):
    """
    Example :
    >>> from semantic.entities import Person, Number, Gender
    >>> _ = ArticleDefiniteContracted(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # à + le = au
    >>> _ = ArticleDefiniteContracted(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.ANY))  # à + les = aux
    >>> _ = ArticleDefiniteContracted(entity=Entity(person=Person.THIRD, number=Number.SINGULAR, gender=Gender.MALE))  # de + le = du
    >>> _ = ArticleDefiniteContracted(entity=Entity(person=Person.THIRD, number=Number.PLURAL, gender=Gender.ANY))  # de + les = des
    """
    entity: Entity
    
    def __str__(self) -> str:
        return f"ART-DEC-{self.entity!s}"
