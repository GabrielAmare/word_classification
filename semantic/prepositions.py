import dataclasses

from semantic import Meaning

__all__ = [
    'Preposition',
]


@dataclasses.dataclass(frozen=True)
class Preposition(Meaning):
    def __str__(self):
        return "PRE"
