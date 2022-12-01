import dataclasses
import re

from semantic.abstract import Meaning
from semantic.entities import Entity
from semantic.times import Time

__all__ = [
    'Verb',
    'VerbInfinite',
    'VerbConjugated',
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


_REGEX_VERB_CONJUGATED = re.compile(
    r"^VER-CON"
    r"-(?P<time>IND-(?:PR|PC|IM|PP|PS|PA|FS|FA)|SUB-(?:PR|PA|IM|PP)|CON-(?:PR|P1|P2)|(?:IMP|PAR|INF|GER)-(?:PR|PA))"
    r"-(?P<entity>[123][SP*][MF*])$"
)


@dataclasses.dataclass(frozen=True)
class VerbConjugated(Verb):
    time: Time
    entity: Entity
    
    @classmethod
    def from_str(cls, expr: str) -> 'VerbConjugated':
        match = _REGEX_VERB_CONJUGATED.match(expr)
        
        if not match:
            raise ValueError(f"Invalid VerbConjugated code {expr!r}.")
        
        return VerbConjugated(
            time=Time.from_str(match.group('time')),
            entity=Entity.from_str(match.group('entity')),
        )
    
    def __str__(self) -> str:
        return f"VER-CON-{self.time!s}-{self.entity!s}"
