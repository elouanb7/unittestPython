import locale

from src import *


class LangueAdapter:
    def __init__(self):
        langue_systeme = locale.getlocale()
        if langue_systeme[0] == "en_GB":
            self.__langue = LangueAnglaise
        else:
            self.__langue = LangueFrancaise

    def get_langue(self):
        return self.__langue


if __name__ == '__main__':
    ohce = Ohce(LangueAdapter().get_langue(), 0)
