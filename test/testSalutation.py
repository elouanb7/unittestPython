import unittest
from src import *


class SalutationTest(unittest.TestCase):
    def test_bonjour(self):
        chaine = "Bonjour !"

        ohce = Ohce()
        resultat = ohce.bonjour()

        self.assertEqual(chaine, resultat)


    def test_au_revoir(self):
        chaine = "Au revoir !"

        ohce = Ohce()
        resultat = ohce.au_revoir()

        self.assertEqual(chaine, resultat)