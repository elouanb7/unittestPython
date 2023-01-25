import unittest
from src import *
from OhceBuilder import *
from parameterized import *


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        ohce = OhceBuilder.default()
        resultat = ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    @parameterized.expand([
        [LangueAnglaise(), "Well done"],
        [LangueFrancaise(), "Bien dit !"],
    ])
    def test_palindrome(self, langue, bien_dit):
        palindrome = "radar"

        ohce = OhceBuilder().ayant_pour_langue(langue).build()

        resultat = ohce.palindrome(palindrome)
        self.assertIn(palindrome, resultat)

        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn(palindrome + bien_dit, resultat_apres_palindrome)


if __name__ == '__main__':
    unittest.main()