from ._CodeTemplate import CodeTemplate


class EntityCode(CodeTemplate):
    """
        Système de classification des entités :

        person :
            1 : 1ère personne
            2 : 2ème personne
            3 : 3ème personne
            D : personne déictique (inclus la 1ère et la 2ème personne)

        number :
            S : singulier
            P : pluriel

        gender :
            M : masculin
            F : féminin

        ces trois informations sont placées dans cet ordre pour former le code, elles sont toutes optionnelles,
        ainsi le code '' est valide et englobe tous les autres.

    """
    persons = ('', '1', '2', '3', 'D')
    numbers = ('', 'S', 'P')
    genders = ('', 'M', 'F')

    @classmethod
    def all(cls):
        """Renvoie la liste ordonnée des codes d'entité valides"""
        for person in cls.persons:
            for number in cls.numbers:
                for gender in cls.genders:
                    yield cls(f"{person}{number}{gender}")

    def __new__(cls, content):
        """Création d'un nouveau code"""
        person, content = (content[0], content[1:]) if content and content[0] in cls.persons else ('', content)
        number, content = (content[0], content[1:]) if content and content[0] in cls.numbers else ('', content)
        gender, content = (content[0], content[1:]) if content and content[0] in cls.genders else ('', content)
        assert not content, f"invalid EntityCode : {person + number + gender + content}"
        instance = super().__new__(cls, person + number + gender)
        instance.person, instance.number, instance.gender = person, number, gender
        return instance

    def contains(self, other):
        """
            Renvoie True si ``other`` est une précision de ``self``
            exemples :
            >>> EntityCode('3S').contains(EntityCode('3SM')) # True
            >>> EntityCode('DM').contains(EntityCode('2PM')) # True
            >>> EntityCode('1SM').contains(EntityCode('1SF')) # False
        """
        assert isinstance(other, EntityCode)
        c1 = other.person in {'1': {'1'}, '2': {'2'}, '3': {'3'}, 'D': {'D', '1', '2'}, '': {'1', '2', '3', 'D', ''}}[
            self.person]
        c2 = other.number in {'S': {'S'}, 'P': {'P'}, '': {'S', 'P', ''}}[self.number]
        c3 = other.gender in {'M': {'M'}, 'F': {'F'}, '': {'M', 'F', ''}}[self.gender]
        return c1 and c2 and c3

    @property
    def plural(self):
        """Renvoie la forme pluriel de ``self``"""
        return EntityCode(self.person + 'P' + self.gender)

    @property
    def singular(self):
        """Renvoie la forme singulière de ``self``"""
        return EntityCode(self.person + 'S' + self.gender)

    @property
    def nogender(self):
        """Renvoie la forme non genrée de ``self``"""
        return EntityCode(self.person + self.number)

    @property
    def male(self):
        """Renvoie la forme masculine de ``self``"""
        return EntityCode(self.person + self.number + 'M')

    @property
    def female(self):
        """Renvoie la forme féminine de ``self``"""
        return EntityCode(self.person + self.number + 'F')

    @property
    def nonumber(self):
        """Renvoie la forme non quantifiée de ``self``"""
        return EntityCode(self.person + self.gender)

    @property
    def first(self):
        """Renvoie la forme à la première personne de ``self``"""
        return EntityCode('1' + self.number + self.gender)

    @property
    def second(self):
        """Renvoie la forme à la duxième personne de ``self``"""
        return EntityCode('2' + self.number + self.gender)

    @property
    def third(self):
        """Renvoie la forme à la troisième personne de ``self``"""
        return EntityCode('3' + self.number + self.gender)

    @property
    def deictic(self):
        """Renvoie la forme à la personne déictique de ``self``"""
        return EntityCode('D' + self.number + self.gender)
