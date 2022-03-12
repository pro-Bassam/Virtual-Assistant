import random
import time
from pygame import mixer


def rollDie():
    mixer.init()
    mixer.music.load(
        "./data/records/rollDie.mpeg")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    return 'it is ' + str(random.randint(1, 6))


print(rollDie())
