class Ohce:

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return self.bonjour() \
            + miroir \
            + (self.bien_dit() if miroir == palindrome else "") \
            + self.au_revoir()

    def bonjour(self):
        return "Bonjour !"

    def bien_dit(self):
        return "Bien dit !"

    def au_revoir(self):
        return "Au revoir !"

    def miroir(self, chaine):
        return chaine[::-1]