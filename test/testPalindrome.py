import unittest
from src import *


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        ohce = Ohce()
        resultat = ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    def test_palindrome(self):
        palindrome = "radar"

        ohce = Ohce()
        chaine_renvoye = ohce.miroir(palindrome)
        self.assertIn(chaine_renvoye, palindrome)

        resultat_apres_palindrome = ohce.palindrome(palindrome)
        self.assertIn(palindrome + "Bien dit !", resultat_apres_palindrome)


if __name__ == '__main__':
    unittest.main()