import unittest
from main import *


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        # QUAND on saisit une chaîne
        resultat = palindrome(chaine)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(chaine[::-1], resultat)

    def test_palindrome(self):
        chaine_palindrome = "radar"

        resultat = palindrome(chaine_palindrome)

        self.assertIn("Bien dit !", resultat)


if __name__ == '__main__':
    unittest.main()
