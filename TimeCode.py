from .EntityCode import EntityCode
from ._CodeTemplate import CodeTemplate


class TimeCode(CodeTemplate):
    moods = ('IND', 'SUB', 'CON', 'IMP', 'PAR', 'INF', 'GER')

    tenses = {
        'IND': ('PR', 'PC', 'IM', 'PP', 'PS', 'PA', 'FS', 'FA'),
        'SUB': ('PR', 'PA', 'IM', 'PP'),
        'CON': ('PR', 'P1', 'P2'),
        'IMP': ('PR', 'PA'),
        'PAR': ('PR', 'PA'),
        'INF': ('PR', 'PA'),
        'GER': ('PR', 'PA')
    }

    @property
    def entitycodes(self):
        """Return the conjugate entities allowed in this time"""
        if self.mood == 'GER':
            return EntityCode('3S'),
        elif self.mood == 'INF':
            return EntityCode(''),
        elif self.mood == 'PAR':
            if self.tense == 'PR':
                return EntityCode('3S'),
            elif self.tense == 'PA':
                return EntityCode('3SM'), \
                       EntityCode('3PM'), \
                       EntityCode('3SF'), \
                       EntityCode('3PF')
            else:
                raise Exception
        elif self.mood == 'IMP' and self.tense == 'PR':
            return EntityCode('2S'), EntityCode('1P'), EntityCode('2P')
        else:
            return EntityCode('1S'), \
                   EntityCode('2S'), \
                   EntityCode('3S'), \
                   EntityCode('1P'), \
                   EntityCode('2P'), \
                   EntityCode('3P')

    @classmethod
    def all(cls):
        """Yield all the TypeCode possibilities"""
        for mood in cls.moods:
            for tense in cls.tenses[mood]:
                yield cls(f"{mood}-{tense}")

    def __new__(cls, content):
        mood, tense = content.split('-', 1)
        assert mood in cls.moods, f"{mood} is not a valid mood"
        assert tense in cls.tenses[mood], f"{tense} is not a valid tense in {mood}"
        instance = super().__new__(cls, content)
        instance.mood, instance.tense = mood, tense
        return instance
