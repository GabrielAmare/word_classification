import abc
import dataclasses

__all__ = [
    'Meaning',
]


@dataclasses.dataclass(frozen=True)
class Meaning(abc.ABC):
    pass
