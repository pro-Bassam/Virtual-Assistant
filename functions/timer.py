import datetime
import time
from pygame import mixer

categores = ['seconds', 'second', 'minutes', 'minute', 'hours', 'hour']


def getTimePeriod(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if wordList[i] in categores:
            if wordList[i] in ['minutes', 'minute']:
                return [int(wordList[i-1]) * 60, f"{wordList[i-1]} {wordList[i]}"]
            elif wordList[i] in ['hours', 'hour']:
                return [int(wordList[i-1]) * 60 * 60, f"{wordList[i-1]} {wordList[i]}"]
            else:
                return [int(wordList[i-1]), f"{wordList[i-1]} {wordList[i]}"]
    return [0, 0]


def setTimer(text):
    timePeriodInSeconds = getTimePeriod(text)[0]
    try:
        if timePeriodInSeconds != 0:
            timePeriodInMilliseconds = int(
                round(time.time() * 1000)) + timePeriodInSeconds * 1000
            _file = open("data/timer.txt", "w")
            _file.write(str(timePeriodInMilliseconds))
            _file.close()

        return getTimePeriod(text)[1]
    except:
        return 0


def runTimer():
    mixer.init()
    mixer.music.load(
        "data/records/timerSound.wav")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

    cancelTimer()


def cancelTimer():
    _file = open("data/timer.txt", "w")
    _file.write('')
    _file.close()


def timerChecker():
    with open("data/timer.txt", 'r') as Text:
        try:
            timerTime = int(Text.read())
        except:
            timerTime = 0

    timeNow = round(time.time() * 1000)
    if timeNow >= timerTime and timerTime != 0:
        runTimer()