import dataclasses
import enum

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
    
    def __str__(self) -> str:
        return f"{self.person.value}{self.number.value}{self.gender.value}"
