import unittest
from src import *
from OhceBuilder import *
from parameterized import *

class SalutationTest(unittest.TestCase):
    @parameterized.expand(
        [
            [LangueAnglaise(), "Hello"],
            [LangueFrancaise(), "Bonjour"],
        ])
    def test_bonjour(self, langue, attendu):
        ohce = OhceBuilder().ayant_pour_langue(langue).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), "Goodbye"],
            [LangueFrancaise(), "Au revoir"],
        ])
    def test_au_revoir(self, langue, attendu):
        ohce = OhceBuilder().ayant_pour_langue(langue).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])