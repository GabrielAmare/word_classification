import dataclasses
import enum
import re

__all__ = [
    'Person',
    'Number',
    'Gender',
    'Entity'
]


class Person(str, enum.Enum):
    FIRST = "1"
    SECOND = "2"
    THIRD = "3"
    ANY = "*"


class Number(str, enum.Enum):
    SINGULAR = "S"
    PLURAL = "P"
    ANY = "*"


class Gender(str, enum.Enum):
    MALE = "M"
    FEMALE = "F"
    ANY = "*"


@dataclasses.dataclass(frozen=True)
class Entity:
    person: Person
    number: Number
    gender: Gender
    
    @classmethod
    def from_str(cls, expr: str) -> 'Entity':
        match = _REGEX_ENTITY.match(expr)
        if not match:
            raise ValueError(f"Invalid {cls.__name__} code {expr!r}")
        
        return Entity(
            person=Person(match.group('person')),
            number=Number(match.group('number')),
            gender=Gender(match.group('gender')),
        )
    
    def __str__(self) -> str:
        return f"{self.person.value}{self.number.value}{self.gender.value}"


_REGEX_ENTITY = re.compile(r"^(?P<person>[123])(?P<number>[SP*])(?P<gender>[MF*])$")
