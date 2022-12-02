import abc
import dataclasses

from semantic import Meaning

__all__ = [
    'Conjunction',
    'ConjunctionCoordination',
    'ConjunctionSubordination',
]


@dataclasses.dataclass(frozen=True)
class Conjunction(Meaning, abc.ABC):
    pass


@dataclasses.dataclass(frozen=True)
class ConjunctionCoordination(Conjunction):
    def __str__(self) -> str:
        return "CON-COO"


@dataclasses.dataclass(frozen=True)
class ConjunctionSubordination(Conjunction):
    def __str__(self) -> str:
        return "CON-SUB"
