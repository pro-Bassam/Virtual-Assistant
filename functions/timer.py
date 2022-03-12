import datetime
import time
from pygame import mixer

categores = ['seconds', 'second', 'minutes', 'minute', 'hours', 'hour']


def getDurition(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if wordList[i].lower() == 'for' or wordList[i].lower() == 'after':
            duration = int(wordList[i+1])
            flag = i+2

    for i in range(flag, len(wordList)):
        if wordList[i] in categores:
            if wordList[i] in ['minutes', 'minute']:
                duration *= 60
                return duration
            elif wordList[i] in ['hours', 'hour']:
                duration *= 60 * 60
                return duration
            else:
                return duration
        else:
            return 0


def setTimer(text):
    durationInSeconds = getDurition(text)
    try:
        timeNowInMilliseconds = int(
            round(time.time() * 1000)) + durationInSeconds * 1000
        f = open("data/timer.txt", "w")
        f.write(str(timeNowInMilliseconds))
        f.close()

        for i in range(0, len(text.split())):
            if text.split()[i].lower() in ['for', 'after']:
                setText = ' '.join(text.split()[i:])

        return setText
    except:
        return 0


def runTimer():
    mixer.init()
    mixer.music.load(
        "data/records/timerSound.wav")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

    f = open("data/timer.txt", "w")
    f.write('')
    f.close()
