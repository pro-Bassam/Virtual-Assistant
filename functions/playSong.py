import os
import pywhatkit
from threading import Thread


def getSongName(text):
    return ' '.join(text.split()[1:])


def play_music(text):
    songName = getSongName(text)
    pywhatkit.playonyt(songName)


def run_music(text):
    music_thread = Thread(target=play_music, args=(text,))
    music_thread.start()


def close_music():
    os.system("taskkill /im chrome.exe /f")
