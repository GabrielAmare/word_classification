import unittest

from semantic import *


class TestFactories(unittest.TestCase):
    def test_meaning(self):
        with open("../resources/examples.csv", mode="r", encoding="utf-8") as file:
            for line in file.read().split('\n'):
                code, word = line.split(',', 1)
                self.assertEqual(code, str(meaning(code)))


if __name__ == '__main__':
    unittest.main()
