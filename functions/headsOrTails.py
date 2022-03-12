
from random import randint


def headsOrTails():
    num = randint(0, 1)
    if(num == 0):
        return 'heads'
    else:
        return 'tails'


# print(headsOrTails())
