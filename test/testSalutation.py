import unittest
from src import *
from OhceBuilder import *
from parameterized import *

class SalutationTest(unittest.TestCase):
    @parameterized.expand(
        [
            [LangueAnglaise(), Constantes.Anglais.HELLO],
            [LangueFrancaise(), Constantes.Francais.BONJOUR],
        ])
    def test_bonjour(self, langue, attendu):
        ohce = OhceBuilder().ayant_pour_langue(langue).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), Constantes.Anglais.GOOD_BYE],
            [LangueFrancaise(), Constantes.Francais.AU_REVOIR],
        ])
    def test_au_revoir(self, langue, attendu):
        ohce = OhceBuilder().ayant_pour_langue(langue).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])