from ._CodeTemplate import CodeTemplate


class VerbCode(CodeTemplate):
    _groups = ('1', '2', '3')
    _auxiliaries = ('E', 'A', '2')
    _pronominals = ('D', 'I', 'N', '2')

    @classmethod
    def all(cls):
        for grp in cls._groups:
            for aux in cls._auxiliaries:
                for prn in cls._pronominals:
                    yield f"{grp}{aux}{prn}"

    def __new__(cls, content):
        grp, aux, prn = content
        assert grp in cls._groups, grp
        assert aux in cls._auxiliaries, aux
        assert prn in cls._pronominals, prn
        instance = super().__new__(cls, content)
        instance.grp, instance.aux, instance.prn = grp, aux, prn
        return instance

    @property
    def group(self):
        return {'1': 1, '2': 2, '3': 3}[self.grp]

    @property
    def auxiliaries(self):
        return {'A': {'avoir'}, 'E': {'être'}, '2': {'avoir', 'être'}}[self.aux]

    @property
    def pronominal(self):
        return {'N': 0, 'D': 1, 'I': 2, '2': 3}[self.prn]
