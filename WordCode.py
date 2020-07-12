from .EntityCode import EntityCode
from .ConjCode import ConjCode
from .TypeCode import TypeCode
from .VerbCode import VerbCode
from ._CodeTemplate import CodeTemplate


class WordCode(CodeTemplate):
    @classmethod
    def all(cls):
        for typecode in TypeCode.all():
            if typecode == 'VER-INF':
                for verbcode in VerbCode.all():
                    yield WordCode(f"{typecode}-{verbcode}")
            elif typecode == 'VER-CON':
                for conjcode in ConjCode.all():
                    yield WordCode(f"{typecode}-{conjcode}")
            elif typecode.startswith('ART'):
                for entitycode in EntityCode.all():
                    if EntityCode('3').contains(entitycode):
                        yield WordCode(f"{typecode}-{entitycode}")
            elif typecode == 'PRO-POS':
                for entitycode in EntityCode.all():
                    for entitycode2 in EntityCode.all():
                        if EntityCode('3').contains(entitycode2):
                            yield WordCode(f"{typecode}-{entitycode}-{entitycode2}")
            elif typecode.startswith('PRO'):
                for entitycode in EntityCode.all():
                    yield WordCode(f"{typecode}-{entitycode}")
            elif typecode == 'NOM-COM':
                for entitycode in EntityCode.all():
                    if EntityCode('3').contains(entitycode):
                        yield WordCode(f"{typecode}-{entitycode}")
            else:
                yield WordCode(f"{typecode}")

    def __new__(cls, content):
        if isinstance(content, int):
            content = cls.uid2code(content)

        if content.startswith('ADJ-NUM'):
            typecode, content = TypeCode(content[:11]), content[12:]
        else:
            typecode, content = TypeCode(content[:7]), content[8:]

        verbcode, conjcode, entitycode, entitycode2 = None, None, None, None

        if typecode == 'VER-INF':
            verbcode = VerbCode(content)
        elif typecode == 'VER-CON':
            conjcode = ConjCode(content)
        elif typecode.startswith('ART'):
            entitycode = EntityCode(content)
        elif typecode == 'PRO-POS':
            entitycode, entitycode2 = map(EntityCode, content.split('-', 1))
        elif typecode.startswith('PRO'):
            entitycode = EntityCode(content)
        elif typecode.startswith('NOM-COM'):
            entitycode = EntityCode(content)
        instance = super().__new__(cls, typecode + ('-' + content if content else ''))
        instance.typecode, instance.verbcode, instance.conjcode, instance.entitycode, instance.entitycode2 = typecode, verbcode, conjcode, entitycode, entitycode2
        return instance

    @property
    def uid(self):
        return self.__class__.code2uid(self)

    @classmethod
    def code2uid(cls, code):
        return tuple(cls.all()).index(code) + 1

    @classmethod
    def uid2code(cls, uid):
        return tuple(cls.all())[uid - 1]

    @property
    def plural(self):
        if self.typecode == 'VER-CON':
            return WordCode(f'{self.typecode}-{self.conjcode.plural}')
        elif self.typecode.startswith('ART'):
            return WordCode(f'{self.typecode}-{self.entitycode.plural}')
        elif self.typecode == 'PRO-POS':
            return WordCode(f'{self.typecode}-{self.entitycode}-{self.entitycode2.plural}')
        elif self.typecode.startswith('NOM-COM'):
            return WordCode(f'{self.typecode}-{self.entitycode.plural}')
        else:
            raise Exception
