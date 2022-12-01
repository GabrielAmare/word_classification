import abc
import dataclasses

from semantic.abstract import Meaning
from semantic.entities import Number, Gender

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
    number: Number
    gender: Gender


@dataclasses.dataclass(frozen=True)
class ArticleDefinite(Article):
    def __str__(self) -> str:
        return f"ART-DEF-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class ArticleIndefinite(Article):
    def __str__(self) -> str:
        return f"ART-IND-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class ArticlePartitive(Article):
    def __str__(self) -> str:
        return f"ART-PAR-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class ArticleDemonstrative(Article):
    def __str__(self) -> str:
        return f"ART-DEM-{self.number.value}{self.gender.value}"


@dataclasses.dataclass(frozen=True)
class ArticleDefiniteContracted(Article):
    def __str__(self) -> str:
        return f"ART-DEC-{self.number.value}{self.gender.value}"
