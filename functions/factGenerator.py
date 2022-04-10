import requests
import time
from pygame import mixer


def factGenerator():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(
        api_url, headers={'X-Api-Key': 'hBga5elo3Ke1FNVX7XJeSg==wiB15TZNhf6UyUc9'})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return "Error:" + response.status_code + response.text


def playFactSound():
    mixer.init()
    mixer.music.load(
        "data/records/fact.wav")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)


print(factGenerator())
