import datetime
import time
import os

from data.keyWords import *
from functions.googleEngine import *
from functions.note import *
from functions.wikioedia import *
from functions.rollDie import *
from functions.headsOrTails import headsOrTails
from functions.playSong import *
from functions.weather import weather
from functions.pickaCard import pickCard
from functions.rockPaperScissors import rockPaperScissors
from functions.factGenerator import factGenerator


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

            # Get Weather Temperature
            if "give me the temperature in" in text and work:
                assistantResponce(weather(text))
                work = 0

            # Pick a Card
            if "pick a card" in text and work:
                assistantResponce(pickCard())
                work = 0

            # Facts Generator
            if "tell me a fact" in text and work:
                assistantResponce(factGenerator())
                work = 0

            # Rock Paper Scissors
            if "rock paper scissors" in text and work:
                assistantResponce(rockPaperScissors())
                work = 0

            #Heads or Tails
            if "flip a coin" in text and work:
                assistantResponce(headsOrTails())
                work = 0

            # roll a die
            if 'roll a die' in text and work:
                assistantResponce(rollDie())
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
