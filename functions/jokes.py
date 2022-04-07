import requests
import time
from pygame import mixer


def getJoke():
    fetchedData = requests.get(
        f"https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if fetchedData.ok:
        joke = fetchedData.json()['joke']
        return joke
    else:
        return 0


def playJokeSound():
    mixer.init()
    mixer.music.load(
        "data/records/jokeAudio.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
