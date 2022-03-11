import pywhatkit

import os
os.add_dll_directory(r'C:/Program Files/VideoLAN/VLC')


def getSongName(text):
    return ' '.join(text.split()[1:])


def play_music(text):
    pywhatkit.playonyt(getSongName(text))
