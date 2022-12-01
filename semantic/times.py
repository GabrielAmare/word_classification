from __future__ import annotations

import dataclasses
import enum
import re

__all__ = [
    'Mood',
    'Tense',
    'Time',
]


class Mood(str, enum.Enum):
    INDICATIVE = "IND"
    SUBJUNCTIVE = "SUB"
    CONDITIONAL = "CON"
    IMPERATIVE = "IMP"
    PARTICIPLE = "PAR"
    INFINITIVE = "INF"
    GERUND = "GER"


class Tense(str, enum.Enum):
    PRESENT = "PR"
    COMPOSED_PAST = "PC"
    IMPERFECT = "IM"
    MORE_THAN_PERFECT = "PP"
    SIMPLE_PAST = "PS"
    ANTERIOR_PAST = "PA"
    SIMPLE_FUTURE = "FS"
    ANTERIOR_FUTURE = "FA"
    PAST = "PA"
    PAST_1 = "P1"
    PAST_2 = "P2"


@dataclasses.dataclass(frozen=True)
class _Time:
    mood: Mood
    tense: Tense
    
    def __str__(self) -> str:
        return f"{self.mood.value}-{self.tense.value}"


_REGEX_TIME = re.compile(r"^IND-(?:PR|PC|IM|PP|PS|PA|FS|FA)"
                         r"|SUB-(?:PR|PA|IM|PP)"
                         r"|CON-(?:PR|P1|P2)"
                         r"|(?:IMP|PAR|INF|GER)-(?:PR|PA)$")


class Time(enum.Enum):
    IND_PR = INDICATIVE_PRESENT = _Time(mood=Mood.INDICATIVE, tense=Tense.PRESENT)
    IND_PC = INDICATIVE_COMPOSED_PAST = _Time(mood=Mood.INDICATIVE, tense=Tense.COMPOSED_PAST)
    IND_IM = INDICATIVE_IMPERFECT = _Time(mood=Mood.INDICATIVE, tense=Tense.IMPERFECT)
    IND_PP = INDICATIVE_MORE_THAN_PERFECT = _Time(mood=Mood.INDICATIVE, tense=Tense.MORE_THAN_PERFECT)
    IND_PS = INDICATIVE_SIMPLE_PAST = _Time(mood=Mood.INDICATIVE, tense=Tense.SIMPLE_PAST)
    IND_PA = INDICATIVE_ANTERIOR_PAST = _Time(mood=Mood.INDICATIVE, tense=Tense.ANTERIOR_PAST)
    IND_FS = INDICATIVE_SIMPLE_FUTURE = _Time(mood=Mood.INDICATIVE, tense=Tense.SIMPLE_FUTURE)
    IND_FA = INDICATIVE_ANTERIOR_FUTURE = _Time(mood=Mood.INDICATIVE, tense=Tense.ANTERIOR_FUTURE)
    
    SUB_PR = SUBJUNCTIVE_PRESENT = _Time(mood=Mood.SUBJUNCTIVE, tense=Tense.PRESENT)
    SUB_PA = SUBJUNCTIVE_PAST = _Time(mood=Mood.SUBJUNCTIVE, tense=Tense.PAST)
    SUB_IM = SUBJUNCTIVE_IMPERFECT = _Time(mood=Mood.SUBJUNCTIVE, tense=Tense.IMPERFECT)
    SUB_PP = SUBJUNCTIVE_MORE_THAN_PERFECT = _Time(mood=Mood.SUBJUNCTIVE, tense=Tense.MORE_THAN_PERFECT)
    
    CON_PR = CONDITIONAL_PRESENT = _Time(mood=Mood.CONDITIONAL, tense=Tense.PRESENT)
    CON_P1 = CONDITIONAL_PAST_1 = _Time(mood=Mood.CONDITIONAL, tense=Tense.PAST_1)
    CON_P2 = CONDITIONAL_PAST_2 = _Time(mood=Mood.CONDITIONAL, tense=Tense.PAST_2)
    
    IMP_PR = IMPERATIVE_PRESENT = _Time(mood=Mood.IMPERATIVE, tense=Tense.PRESENT)
    IMP_PA = IMPERATIVE_PAST = _Time(mood=Mood.IMPERATIVE, tense=Tense.PAST)
    
    PAR_PR = PARTICIPLE_PRESENT = _Time(mood=Mood.PARTICIPLE, tense=Tense.PRESENT)
    PAR_PA = PARTICIPLE_PAST = _Time(mood=Mood.PARTICIPLE, tense=Tense.PAST)
    
    INF_PR = INFINITIVE_PRESENT = _Time(mood=Mood.INFINITIVE, tense=Tense.PRESENT)
    INF_PA = INFINITIVE_PAST = _Time(mood=Mood.INFINITIVE, tense=Tense.PAST)
    
    GER_PR = GERUND_PRESENT = _Time(mood=Mood.GERUND, tense=Tense.PRESENT)
    GER_PA = GERUND_PAST = _Time(mood=Mood.GERUND, tense=Tense.PAST)
    
    @classmethod
    def from_str(cls, expr: str) -> Time:
        assert _REGEX_TIME.match(expr), f"Invalid Time code provided {expr!r}"
        return Time[expr.replace('-', '_')]
    
    def __str__(self) -> str:
        return str(self.value)
