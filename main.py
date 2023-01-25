import locale

from src import *


class LangueAdapter:
    def __init__(self):
        langue_systeme = locale.getlocale()
        if langue_systeme == "en_GB":
            self.__langue = langue_systeme
        else:
            self.__langue = "fr_FR"


if __name__ == '__main__':
    ohce = Ohce(LangueAdapter())