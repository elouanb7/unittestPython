import sys
from datetime import datetime


def main():
    is_running = True
    date = datetime.now()
    while is_running:
        print(hello(date))
        chaine = input("Entrez la chaine de caractères de votre choix :\n")
        print(palindrome(chaine))
        if input("Voulez vous quitter ? [y/N]\n") == "y" or "Y":
            is_running = False
    print(close(date))
    sys.exit()

def palindrome(chaine):
    if chaine == chaine[::-1]:
        return 'Bien dit !'
    else:
        return chaine[::-1]


def close(date):
    if date.hour < 12:
        return "Bonne journée !"
    else:
        return "Bonne après-midi !"



def hello(date):
    if date.hour < 12:
        return "Good morning"
    else:
        return "Good afternoon"


if __name__ == '__main__':
    main()
