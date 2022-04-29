import datetime
import time
import os
from data.keyWords import *
from functions.googleEngine import *
from functions.note import *
from functions.playSong import *
from functions.timer import cancelTimer, setTimer, timerChecker
from functions.translation_to_french import trans
from functions.wikioedia import *
from functions.rollDie import *
from functions.headsOrTails import headsOrTails
from functions.playSong import *
from functions.weather import weather
from functions.pickaCard import pickCard
from functions.rockPaperScissors import rockPaperScissors
from functions.factGenerator import factGenerator, playFactSound
from functions.currancy_converter import currency
from functions.jokes import getJoke, playJokeSound
from functions.math import *


# RUNNING
terminator = 1
assistantResponce("boot up started, waiting for your call")
while terminator:
    # Record audio as string
    text = recordAduio()

    # Run timer if the time ended
    timerChecker()

    # Start functioning when it is called
    for phrase in WAKE_WORDS:
        if phrase in text:
            work = 1
            assistantResponce("yes")
            text = recordAduio()

            # personal info
            for phrase in NAME_KEYWORDS:
                if phrase in text and work:
                    for answer in PERSONAL_INFORMATIONS:
                        assistantResponce(answer)
                        work = 0

            # personal features
            for phrase in FEATURES_WORDS:
                if phrase in text and work:
                    for answer in LIST_OF_FEATURES:
                        assistantResponce(answer)
                        work = 0

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

            # Tell me a Joke
            for phrase in JOKES_KEY_WORDS:
                if phrase in text and work:
                    response = getJoke()
                    if response != 0:
                        assistantResponce(response)
                        playJokeSound()
                        work = 0
                    else:
                        assistantResponce("Sorry can you try later")

            # cancel a timer
            for phrase in CANCEL_TIMER_KEY_WORDS:
                if phrase in text and work:
                    cancelTimer()
                    assistantResponce("the timer is canceled successfully")
                    work = 0

            # set a timer
            for phrase in TIMER_KEY_WORDS:
                if phrase in text and work:
                    assistantResponce("What is the period")
                    timePeriod = recordAduio()
                    result = setTimer(timePeriod)
                    if result == 0:
                        assistantResponce("can not set this timer try again")
                    else:
                        assistantResponce(
                            f"Timer is seted successfully for {result}")
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
                playFactSound()
                work = 0

            # Rock Paper Scissors
            if "rock paper scissors" in text and work:
                assistantResponce(rockPaperScissors())
                work = 0

            # Heads or Tails
            if "flip a coin" in text and work:
                assistantResponce(headsOrTails())
                work = 0

            # roll a die
            if 'roll a die' in text and work:
                assistantResponce(rollDie())
                work = 0

            # cancel music
            for phrase in CANCEL_MUSIC_KEY_WORDS:
                if phrase in text and work:
                    close_music()
                    assistantResponce("the music is canceled successfully")
                    work = 0

            # Play a music by name
            if 'play' in text and work:
                run_music(text)
                work = 0

            # Make a note
            for phrase in NOTE_STRS:
                if phrase in text and work:
                    assistantResponce("What would you like me to write down?")
                    write_down = recordAduio()
                    makeNote(write_down)
                    assistantResponce("I've made a note of that.")
                    work = 0

            # Translate to French
            for phrase in TRANSLATE_KEY_WORDS:
                if phrase in text and work:
                    assistantResponce("I am listening.")
                    sentence = recordAduio()
                    responce = trans(sentence)
                    assistantResponce(responce)
                    work = 0

            # Math Function
            for phrase in MATH_WORDS:
                if phrase in text and work:
                    responce = calculate(text)
                    assistantResponce(responce)
                    work = 0

            # Currency Converter
            for phrase in CUURENCY_KEY_WORDS:
                if phrase in text and work:
                    assistantResponce("what amount")
                    amount = recordAduio()
                    amount = int(amount)
                    responce = currency(text, amount)
                    assistantResponce(responce)
                    work = 0

            # Terminate the running
            # for phrase in BREAK_WORDS:
            #     if phrase in text and work:
            #         terminator = 0
            #         assistantResponce("shutting down the system")
            #         assistantResponce(
            #             "you will need to power off and on again")
            #         quit()

            if work == 1:
                assistantResponce("Sorry I don't understand")
