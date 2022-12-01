import unittest

from semantic.entities import *
from semantic.pronouns import *


class TestPronouns(unittest.TestCase):
    def test_pronoun_possessive(self):
        dictionary = {
            'le mien': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
            ),
            'le tien': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
            ),
            'le sien': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
            ),
            'la mienne': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
            ),
            'la tienne': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
            ),
            'la sienne': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.FEMALE,
            ),
            'les miens': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.MALE,
            ),
            'les tiens': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.MALE,
            ),
            'les siens': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.MALE,
            ),
            'les miennes': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
            ),
            'les tiennes': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
            ),
            'les siennes': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.SINGULAR,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
            ),
            'le nôtre': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
            ),
            'la nôtre': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
            ),
            'les nôtres': PronounPossessive(
                owner_person=Person.FIRST,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
            ),
            'le vôtre': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
            ),
            'la vôtre': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
            ),
            'les vôtres': PronounPossessive(
                owner_person=Person.SECOND,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
            ),
            'le leur': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.SINGULAR,
                owned_gender=Gender.MALE,
            ),
            'la leur': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.FEMALE,
            ),
            'les leurs': PronounPossessive(
                owner_person=Person.THIRD,
                owner_number=Number.PLURAL,
                owned_number=Number.PLURAL,
                owned_gender=Gender.ANY,
            ),
        }
    
    def test_pronoun_demonstrative(self):
        dictionary = {
            'celui': PronounDemonstrative(
                number=Number.SINGULAR,
                gender=Gender.MALE,
            ),
            'celle': PronounDemonstrative(
                number=Number.SINGULAR,
                gender=Gender.FEMALE,
            ),
            'ceux': PronounDemonstrative(
                number=Number.PLURAL,
                gender=Gender.MALE,
            ),
            'celles': PronounDemonstrative(
                number=Number.PLURAL,
                gender=Gender.FEMALE,
            ),
            'ceci': PronounDemonstrative(
                number=Number.ANY,
                gender=Gender.ANY,
            ),
        }
    
    def test_pronoun_indefinite(self):
        dictionary = {
            'aucun': PronounIndefinite(
                number=Number.SINGULAR,
                gender=Gender.MALE,
            ),
            'aucune': PronounIndefinite(
                number=Number.SINGULAR,
                gender=Gender.FEMALE,
            ),
            'certains': PronounIndefinite(
                number=Number.PLURAL,
                gender=Gender.MALE,
            ),
            'certaines': PronounIndefinite(
                number=Number.PLURAL,
                gender=Gender.FEMALE,
            ),
            'autre': PronounIndefinite(
                number=Number.SINGULAR,
                gender=Gender.ANY,
            ),
            'autres': PronounIndefinite(
                number=Number.PLURAL,
                gender=Gender.ANY,
            ),
            'autrui': PronounIndefinite(
                number=Number.ANY,
                gender=Gender.ANY,
            ),
            'plusieurs': PronounIndefinite(
                number=Number.PLURAL,
                gender=Gender.ANY,
            ),
            "quelqu'un": PronounIndefinite(
                number=Number.SINGULAR,
                gender=Gender.MALE,
            ),
            "quelqu'une": PronounIndefinite(
                number=Number.SINGULAR,
                gender=Gender.FEMALE,
            ),
            "quelques-uns": PronounIndefinite(
                number=Number.PLURAL,
                gender=Gender.MALE,
            ),
            "quelques-unes": PronounIndefinite(
                number=Number.PLURAL,
                gender=Gender.FEMALE,
            ),
        }
    
    def test_pronoun_impersonal(self):
        dictionary = {
            'il': PronounImpersonal(
                person=Person.THIRD,
                number=Number.SINGULAR,
                gender=Gender.MALE,
            )
        }
    
    def test_pronoun_reflexive(self):
        dictionary = {
            "me": PronounReflexive(person=Person.FIRST, number=Number.SINGULAR),
            "m'": PronounReflexive(person=Person.FIRST, number=Number.SINGULAR),
            "moi": PronounReflexive(person=Person.FIRST, number=Number.SINGULAR),
            "te": PronounReflexive(person=Person.SECOND, number=Number.SINGULAR),
            "t'": PronounReflexive(person=Person.SECOND, number=Number.SINGULAR),
            "toi": PronounReflexive(person=Person.SECOND, number=Number.SINGULAR),
            "nous": PronounReflexive(person=Person.FIRST, number=Number.PLURAL),
            "vous": PronounReflexive(person=Person.SECOND, number=Number.PLURAL),
            "se": PronounReflexive(person=Person.THIRD, number=Number.ANY),
            "s'": PronounReflexive(person=Person.THIRD, number=Number.ANY),
            "soi": PronounReflexive(person=Person.THIRD, number=Number.ANY),
        }


if __name__ == '__main__':
    unittest.main()
