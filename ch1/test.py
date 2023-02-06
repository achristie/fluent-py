import deck
import vector
from random import choice


def main():
    d = deck.FrenchDeck()
    print(choice(d))

    v = vector.Vector(100, 200)
    print(v * 2)


main()
