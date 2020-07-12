from .TimeCode import TimeCode
from .EntityCode import EntityCode
from ._CodeTemplate import CodeTemplate


class ConjCode(CodeTemplate):
    @classmethod
    def all(cls):
        for timecode in TimeCode.all():
            for entitycode in timecode.entitycodes:
                if entitycode:
                    yield cls(f"{timecode}-{entitycode}")
                else:
                    yield cls(f"{timecode}")

    @classmethod
    def of(cls, timecode: (TimeCode, str)):
        if isinstance(timecode, str):
            timecode = TimeCode(timecode)
        for entitycode in timecode.entitycodes:
            if entitycode:
                yield cls(f"{timecode}-{entitycode}")
            else:
                yield cls(f"{timecode}")

    def __new__(cls, content):
        timecode, entitycode = TimeCode(content[:6]), EntityCode(content[7:] if len(content) > 6 else '')
        assert entitycode in timecode.entitycodes
        instance = super().__new__(cls, content)
        instance.timecode, instance.entitycode = timecode, entitycode
        return instance
    
    @property
    def plural(self):
        if self.timecode == 'PAR-PA':
            return ConjCode(f'{self.timecode}-{self.entitycode.plural}')
        else:
            raise Exception
