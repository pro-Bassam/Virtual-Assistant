import random
import time
from pygame import mixer


def flipCoin():
    mixer.init()
    mixer.music.load(
        "records/flipCoin.mpeg")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    return 'it is ' + ('Head' if random.randint(0, 1) == 1 else 'Tail')


def rollDie():
    mixer.init()
    mixer.music.load(
        "records/rollDie.mpeg")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    return 'it is ' + str(random.randint(1, 6))
