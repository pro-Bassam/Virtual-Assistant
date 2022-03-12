import datetime
import time
import os

from data.keyWords import *
from functions.googleEngine import *
from functions.note import *
from functions.wikioedia import *
from functions.rollaDic import rollADic
from functions.headsOrTails import headsOrTails
from functions.playSong import *


# RUNNING
terminator = 1
assistantResponce("boot up started, waiting for your call")
while terminator:
    # Record audio as string
    text = recordAduio()

    # Start functioning when it is called
    for phrase in WAKE_WORDS:
        if phrase in text:
            work = 1
            assistantResponce("yes")
            text = recordAduio()

            # Get the current date
            for phrase in TODAY_DATE:
                if phrase in text and work:
                    today = datetime.date.today()
                    assistantResponce(today)
                    work = 0

            # Search in wikipedia
            for phrase in SEARCH_KEY_WORDS:
                if phrase in text and work:
                    responce = searchAbout(text)
                    assistantResponce(responce)
                    work = 0

            # Roll A Dic
            if "roll a dic" in text and work:
                assistantResponce(rollADic())
                work = 0

            #Heads or Tails
            if "heads or tails" in text and work:
                assistantResponce(headsOrTails())
                work = 0

            # Play a music by name
            if 'play' in text and work:
                play_music(text)
                work = 0

            # Make a note
            for phrase in NOTE_STRS:
                if phrase in text and work:
                    assistantResponce("What would you like me to write down?")
                    write_down = recordAduio()
                    makeNote(write_down)
                    assistantResponce("I've made a note of that.")
                    work = 0

            # Terminate the running
            for phrase in BREAK_WORDS:
                if phrase in text and work:
                    terminator = 0
                    assistantResponce("shutting down the system")
                    assistantResponce(
                        "you will need to power off and on again")
                    quit()
            if work == 1:
                assistantResponce("Sorry I don't understand")
