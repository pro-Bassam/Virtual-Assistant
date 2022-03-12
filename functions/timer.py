from word2number import w2n
import time
from pygame import mixer


def getDurition(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if wordList[i].lower() == 'for' or wordList[i].lower() == 'after':
            duration = int(wordList[i+1])
            flag = i+1
            for i in range(flag, len(wordList)):
                if wordList[i] == 'seconds' or wordList[i] == 'minutes' or wordList[i] == 'hours':
                    if wordList[i] == 'minutes':
                        duration *= 60
                    elif wordList[i] == 'hours':
                        duration *= 60 * 60
                    return duration


def setTimer(text):
    duration = getDurition(text)
    try:
        time.sleep(duration)
        mixer.init()
        mixer.music.load(
            "records/timerSound.wav ")
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        return 1
    except:
        print('can not set the timer try again')
        return 0


setTimer('set timer for 2 seconds')
