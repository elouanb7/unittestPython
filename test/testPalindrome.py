import unittest
from utilities import *
from parameterized import *


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        ohce = OhceBuilder.default()
        resultat = ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    @parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE],
        [LangueFrancaise(), Constantes.Francais.BIEN_DIT],
    ])
    def test_palindrome(self, langue, bien_dit):
        palindrome = "kayak"
        ohce = OhceBuilder().ayant_pour_langue(langue).build()

        resultat = ohce.palindrome(palindrome)
        self.assertIn(palindrome, resultat)

        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn(palindrome + bien_dit, resultat_apres_palindrome)

    def test_non_palindrome(self):
        langue = LangueSpy()
        ohce = OhceBuilder().ayant_pour_langue(langue).build()

        ohce.palindrome("Elouan")

        self.assertEqual(0, langue.nb_bien_dit)


if __name__ == '__main__':
    unittest.main()
