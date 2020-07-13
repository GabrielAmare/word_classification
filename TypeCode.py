from ._CodeTemplate import CodeTemplate


class TypeCode(CodeTemplate):
    g_classes = ("NOM", "ART", "ADJ", "PRO", "VER", "ADV", "PRE", "CON", "INT")

    g_subclasses = {
        "NOM": ("PRO", "COM"),
        "ART": ("DEF", "IND", "PAR", "DEM", "DEC"), # DEC : DEfini Contracté
        "ADJ": ("QUA", "REL", "NUM-CAR", "NUM-ORD", "IND"),
        "PRO": ("PER", "ADV", "REL", "INT", "POS", "DEM", "IND", "NUM", "IMP", "QUA", "ADJ", "SUB", "REF"),
        "VER": ("INF", "CON"),
        "ADV": ("MAN", "LIE", "TEM", "ASP", "LOG", "EXP", "ANA"),
        "PRE": (),
        "CON": ("COO", "SUB"),
        "INT": ("STR", "ONO", "EMP")
    }

    @classmethod
    def all(cls):
        """Yield all the TypeCode possibilities"""
        for g_class in cls.g_classes:
            g_subclasses = cls.g_subclasses[g_class]
            if g_subclasses:
                for g_subclass in g_subclasses:
                    yield cls(f"{g_class}-{g_subclass}")
            else:
                yield cls(f"{g_class}")

    def __new__(cls, content):
        g_class, g_subclass = content.split('-', 1) if '-' in content else (str(content), '')
        assert g_class in cls.g_classes
        assert not cls.g_subclasses[g_class] or g_subclass in cls.g_subclasses[g_class]
        instance = super().__new__(cls, content)
        instance.g_class, instance.g_subclass = g_class, g_subclass
        return instance
