from random import randint
from pygame import mixer
import time


def headsOrTails():
    mixer.init()
    mixer.music.load("data/records/flip_coin.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

    num = randint(0, 1)
    if(num == 0):
        return 'heads'
    else:
        return 'tails'


# print(headsOrTails())
