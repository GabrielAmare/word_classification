import abc
import dataclasses

from semantic import Meaning

__all__ = [
    'Adverb',
    'AdverbManner',
    'AdverbPlace',
    'AdverbTime',
    'AdverbAspect',
    'AdverbLogical',
    'AdverbExpletive',
    'AdverbAnaphoric',
    'AdverbNegation',
]


@dataclasses.dataclass(frozen=True)
class Adverb(Meaning, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class AdverbManner(Adverb):
    def __str__(self) -> str:
        return "ADV-MAN"


@dataclasses.dataclass(frozen=True)
class AdverbPlace(Adverb):
    def __str__(self) -> str:
        return "ADV-LIE"


@dataclasses.dataclass(frozen=True)
class AdverbTime(Adverb):
    def __str__(self) -> str:
        return "ADV-TEM"


@dataclasses.dataclass(frozen=True)
class AdverbAspect(Adverb):
    def __str__(self) -> str:
        return "ADV-ASP"


@dataclasses.dataclass(frozen=True)
class AdverbLogical(Adverb):
    def __str__(self) -> str:
        return "ADV-LOG"


@dataclasses.dataclass(frozen=True)
class AdverbExpletive(Adverb):
    def __str__(self) -> str:
        return "ADV-EXP"


@dataclasses.dataclass(frozen=True)
class AdverbAnaphoric(Adverb):
    def __str__(self) -> str:
        return "ADV-ANA"


@dataclasses.dataclass(frozen=True)
class AdverbNegation(Adverb):
    def __str__(self) -> str:
        return "ADV-NEG"
