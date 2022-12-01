import dataclasses
import re

from semantic.abstract import Meaning

__all__ = [
    'Verb',
    'VerbInfinite',
]


@dataclasses.dataclass(frozen=True)
class Verb(Meaning):
    pass


_REGEX_VERB_INFINITE = re.compile(r"^VER-INF-(?P<group>[123])(?P<auxiliaries>[EA2])(?P<pronominal>[0DI2])$")


@dataclasses.dataclass(frozen=True)
class VerbInfinite(Verb):
    group: int
    auxiliary_be: bool
    auxiliary_have: bool
    pronominal_direct: bool
    pronominal_indirect: bool
    
    def __post_init__(self):
        assert self.group in (1, 2, 3)
        assert self.auxiliary_be or self.auxiliary_have
    
    def __str__(self):
        auxiliaries = ' EA2'[self.auxiliary_be + 2 * self.auxiliary_have]
        pronominal = '0DI2'[self.pronominal_direct + 2 * self.pronominal_indirect]
        return f"VER-INF-{self.group}{auxiliaries}{pronominal}"
    
    @classmethod
    def from_str(cls, expr: str) -> 'VerbInfinite':
        match = _REGEX_VERB_INFINITE.match(expr)
        if not match:
            raise ValueError(f"Invalid VerbInfinite code {expr!r}.")
        
        group = int(match.group('group'))
        
        auxiliaries = match.group('auxiliaries')
        auxiliary_be = auxiliaries in ('E', '2')
        auxiliary_have = auxiliaries in ('A', '2')
        
        pronominal = match.group('pronominal')
        pronominal_direct = pronominal in ('D', '2')
        pronominal_indirect = pronominal in ('I', '2')
        
        return VerbInfinite(
            group=group,
            auxiliary_be=auxiliary_be,
            auxiliary_have=auxiliary_have,
            pronominal_direct=pronominal_direct,
            pronominal_indirect=pronominal_indirect,
        )
