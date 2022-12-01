import re

from .abstract import *
from .adjectives import *
from .articles import *
from .entities import *
from .nouns import *
from .pronouns import *

__all__ = [
    'meaning',
]
_PATTERNS = {
    NounCommon: re.compile(r"^NOM-COM-(?P<number>[SP*])(?P<gender>[MF*])$"),
    NounProper: re.compile(r"^NOM-PRO-(?P<number>[SP*])(?P<gender>[MF*])$"),
    ArticleDefinite: re.compile(r"^ART-DEF-(?P<number>[SP*])(?P<gender>[MF*])$"),
    ArticleIndefinite: re.compile(r"^ART-IND-(?P<number>[SP*])(?P<gender>[MF*])$"),
    ArticlePartitive: re.compile(r"^ART-PAR-(?P<number>[SP*])(?P<gender>[MF*])$"),
    ArticleDemonstrative: re.compile(r"^ART-DEM-(?P<number>[SP*])(?P<gender>[MF*])$"),
    ArticleDefiniteContracted: re.compile(r"^ART-DEC-(?P<number>[SP*])(?P<gender>[MF*])$"),
    AdjectiveQualifying: re.compile(r"^ADJ-QUA-(?P<number>[SP*])(?P<gender>[MF*])$"),
    AdjectiveRelative: re.compile(r"^ADJ-REL-(?P<number>[SP*])(?P<gender>[MF*])$"),
    AdjectiveIndefinite: re.compile(r"^ADJ-IND-(?P<number>[SP*])(?P<gender>[MF*])$"),
    AdjectiveNumeralCardinal: re.compile(r"^ADJ-NUM-(?P<number>[SP*])(?P<gender>[MF*])-CAR-(?P<value>0|[1-9]\d*)$"),
    AdjectiveNumeralOrdinal: re.compile(r"^ADJ-NUM-(?P<number>[SP*])(?P<gender>[MF*])-ORD-(?P<value>0|[1-9]\d*)$"),
    AdjectivePossessive: re.compile(r"^ADJ-POS-(?P<number>[SP*])(?P<gender>[MF*])"
                                    r"-(?P<owner_person>[123])(?P<owner_number>[SP*])"
                                    r"-(?P<tonic>[NT])$"),
}


def meaning(code: str) -> Meaning:
    """Main factory that translate a str code into the correct Meaning object."""
    if code.startswith("NOM-COM-"):
        m = _PATTERNS[NounCommon].match(code)
        return NounCommon(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("NOM-PRO-"):
        m = _PATTERNS[NounProper].match(code)
        return NounProper(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ART-DEF-"):
        m = _PATTERNS[ArticleDefinite].match(code)
        return ArticleDefinite(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ART-IND-"):
        m = _PATTERNS[ArticleIndefinite].match(code)
        return ArticleIndefinite(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ART-PAR-"):
        m = _PATTERNS[ArticlePartitive].match(code)
        return ArticlePartitive(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ART-DEM-"):
        m = _PATTERNS[ArticleDemonstrative].match(code)
        return ArticleDemonstrative(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ART-DEC-"):
        m = _PATTERNS[ArticleDefiniteContracted].match(code)
        return ArticleDefiniteContracted(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ADJ-QUA-"):
        m = _PATTERNS[AdjectiveQualifying].match(code)
        return AdjectiveQualifying(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ADJ-REL-"):
        m = _PATTERNS[AdjectiveRelative].match(code)
        return AdjectiveRelative(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ADJ-IND-"):
        m = _PATTERNS[AdjectiveIndefinite].match(code)
        return AdjectiveIndefinite(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("ADJ-NUM-") and '-CAR-' in code:
        m = _PATTERNS[AdjectiveNumeralCardinal].match(code)
        return AdjectiveNumeralCardinal(
            number=Number(m.group('number')),
            gender=Gender(m.group('gender')),
            value=int(m.group('value'))
        )
    elif code.startswith("ADJ-NUM-") and '-ORD-' in code:
        m = _PATTERNS[AdjectiveNumeralOrdinal].match(code)
        return AdjectiveNumeralOrdinal(
            number=Number(m.group('number')),
            gender=Gender(m.group('gender')),
            value=int(m.group('value'))
        )
    elif code.startswith("ADJ-POS-"):
        m = _PATTERNS[AdjectivePossessive].match(code)
        return AdjectivePossessive(
            number=Number(m.group('number')),
            gender=Gender(m.group('gender')),
            owner_person=Person(m.group('owner_person')),
            owner_number=Number(m.group('owner_number')),
            tonic=m.group('tonic') == 'T',
        )
    else:
        raise ValueError(code)
