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
    pass


@dataclasses.dataclass(frozen=True)
class ConjunctionSubordination(Conjunction):
    pass
