from pytube import YouTube
import time
import pyautogui
import pywhatkit


def getSongName(text):
    return ' '.join(text.split()[1:])


def play_music(text):
    songName = getSongName(text)
    url = pywhatkit.playonyt(songName)
    yt = YouTube(url)
    time.sleep(yt.length + 20)
    pyautogui.hotkey('ctrl', 'w')
