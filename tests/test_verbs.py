import unittest

from semantic.verbs import *


class TestVerbs(unittest.TestCase):
    def test_verb_infinite(self):
        for group in (1, 2, 3):
            for auxiliary_be in (False, True):
                for auxiliary_have in (False, True):
                    if auxiliary_be or auxiliary_have:
                        for pronominal_direct in (False, True):
                            for pronominal_indirect in (False, True):
                                verb_infinite = VerbInfinite(
                                    group=group,
                                    auxiliary_be=auxiliary_be,
                                    auxiliary_have=auxiliary_have,
                                    pronominal_direct=pronominal_direct,
                                    pronominal_indirect=pronominal_indirect,
                                )
                                self.assertEqual(verb_infinite, VerbInfinite.from_str(str(verb_infinite)))


if __name__ == '__main__':
    unittest.main()
