import speech_recognition as sr
import pyttsx3

# Record audio as string


def recordAduio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print(data.lower())
    except sr.UnknownValueError:
        # assistantResponce("Sorry, I don't understand")
        pass
    except sr.RequestError as e:
        assistantResponce(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return data.lower()


# Responce in a voice
def assistantResponce(text):
    engine = pyttsx3.init()

    """ RATE"""
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 173)     # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty(
        'volume')  # getting to know current volume level (min=0 and max=1)
    # setting up volume level  between 0 and 1
    engine.setProperty('volume', 1.0)

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # changing index, changes voices. o for male and 1 for female
    engine.setProperty('voice', voices[1].id)

    print(text)
    engine.say(text)
    engine.runAndWait()
