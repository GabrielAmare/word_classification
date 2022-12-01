import dataclasses

from semantic import Meaning

__all__ = [
    'Preposition',
]


@dataclasses.dataclass(frozen=True)
class Preposition(Meaning):
    pass
