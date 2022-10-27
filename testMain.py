import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_hello(self):
        hour = datetime.now().replace(hour=11)
        self.assertEqual("Good morning", hello(hour))
        hour = datetime.now().replace(hour=15)
        self.assertEqual("Good afternoon", hello(hour))

    def test_close(self):
        hour = datetime.now().replace(hour=11)
        self.assertEqual("Bonne journée !", close(hour))
        hour = datetime.now().replace(hour=15)
        self.assertEqual("Bonne après-midi !", close(hour))

    def test_revert(self):
        resultat = revert("abcd")
        self.assertEqual("dcba", resultat)
        resultat = revert("rotor")
        self.assertEqual("Bien dit !", resultat)


if __name__ == '__main__':
    unittest.main()
