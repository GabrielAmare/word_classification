import re

from .abstract import *
from .adjectives import *
from .adverbs import *
from .articles import *
from .conjunctions import *
from .entities import *
from .nouns import *
from .prepositions import *
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
    PronounPersonal: re.compile(r"^PRO-PER-(?P<person>[123])(?P<number>[SP*])(?P<gender>[MF*])$"),
    PronounRelativeInvariable: re.compile(r"^PRO-REL-INV$"),
    PronounRelativeVariable: re.compile(r"^PRO-REL-VAR-(?P<number>[SP*])(?P<gender>[MF*])$"),
    PronounPossessive: re.compile(r"^PRO-POS-(?P<number>[SP*])(?P<gender>[MF*])"
                                  r"-(?P<owner_person>[123])(?P<owner_number>[SP*])$"),
    PronounDemonstrative: re.compile(r"^PRO-DEM-(?P<number>[SP*])(?P<gender>[MF*])$"),
    PronounIndefinite: re.compile(r"^PRO-IND-(?P<number>[SP*])(?P<gender>[MF*])$"),
    PronounImpersonal: re.compile(r"^PRO-IMP-(?P<person>[123])(?P<number>[SP*])(?P<gender>[MF*])$"),
    PronounReflexive: re.compile(r"^PRO-REF-(?P<person>[123])(?P<number>[SP*])$"),
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
    elif code.startswith("PRO-PER-"):
        cls = PronounPersonal
        m = _PATTERNS[cls].match(code)
        return cls(person=Person(m.group('person')), number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code == "PRO-ADV":
        return PronounAdverbial()
    elif code == "PRO-REL-INV":
        return PronounRelativeInvariable()
    elif code.startswith("PRO-REL-VAR-"):
        m = _PATTERNS[PronounRelativeVariable].match(code)
        return PronounRelativeVariable(
            number=Number(m.group('number')),
            gender=Gender(m.group('gender')),
        )
    elif code == "PRO-INT":
        return PronounInterrogative()
    elif code.startswith("PRO-POS-"):
        m = _PATTERNS[PronounPossessive].match(code)
        return PronounPossessive(
            number=Number(m.group('number')),
            gender=Gender(m.group('gender')),
            owner_person=Person(m.group('owner_person')),
            owner_number=Number(m.group('owner_number')),
        )
    elif code.startswith("PRO-DEM-"):
        cls = PronounDemonstrative
        m = _PATTERNS[cls].match(code)
        return cls(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code.startswith("PRO-IND-"):
        cls = PronounIndefinite
        m = _PATTERNS[cls].match(code)
        return cls(number=Number(m.group('number')), gender=Gender(m.group('gender')))
    elif code == "PRO-IMP":
        return PronounImpersonal()
    elif code == "PRE":
        return Preposition()
    elif code == "ADV-MAN":
        return AdverbManner()
    elif code == "ADV-LIE":
        return AdverbPlace()
    elif code == "ADV-TEM":
        return AdverbTime()
    elif code == "ADV-LOG":
        return AdverbLogical()
    elif code == "ADV-EXP":
        return AdverbExpletive()
    elif code == "ADV-NEG":
        return AdverbNegation()
    elif code == "CON-COO":
        return ConjunctionCoordination()
    elif code == "CON-SUB":
        return ConjunctionSubordination()
    elif code.startswith("PRO-REF-"):
        cls = PronounReflexive
        m = _PATTERNS[cls].match(code)
        return cls(person=Person(m.group('person')), number=Number(m.group('number')))
    else:
        raise ValueError(code)
