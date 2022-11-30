import unittest

from semantic.adjectives import *
from semantic.entities import *


class TestAdjectives(unittest.TestCase):
    def test_adjective_possessive(self):
        dictionary = {
            'mon': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
                tonic=False,
            ),
            'ton': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
                tonic=False,
            ),
            'son': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
                tonic=False,
            ),
            'ma': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
                tonic=False,
            ),
            'ta': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
                tonic=False,
            ),
            'sa': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
                tonic=False,
            ),
            'mes': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'tes': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'ses': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'notre': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'nos': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'votre': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'vos': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'leur': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
            'leurs': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=False,
            ),
        }
        
        tonics = {
            'mien': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
                tonic=True,
            ),
            'tien': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
                tonic=True,
            ),
            'sien': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
                tonic=True,
            ),
            'nôtre': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.ANY,
                tonic=True,
            ),
            'vôtre': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.ANY,
                tonic=True,
            ),
            'leur': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.ANY,
                tonic=True,
            ),
            'miens': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.MALE,
                tonic=True,
            ),
            'tiens': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.MALE,
                tonic=True,
            ),
            'siens': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.MALE,
                tonic=True,
            ),
            'nôtres': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=True,
            ),
            'vôtres': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=True,
            ),
            'leurs': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
                tonic=True,
            ),
            'mienne': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
                tonic=True,
            ),
            'tienne': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
                tonic=True,
            ),
            'sienne': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
                tonic=True,
            ),
            'miennes': AdjectivePossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
                tonic=True,
            ),
            'tiennes': AdjectivePossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
                tonic=True,
            ),
            'siennes': AdjectivePossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
                tonic=True,
            ),
        }


if __name__ == '__main__':
    unittest.main()
