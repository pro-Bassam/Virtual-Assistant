import wikipedia

# for testing
# what is biology
# who is mark zuckerberg

# GET A PERSON FIRST AND LAST NAME FROM THE TEXT
def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if i+3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            print()
            return wordList[i+2] + ' ' + wordList[i+3]

# GET object FROM THE TEXT
def getObject(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if wordList[i].lower() == 'what' and wordList[i+1].lower() == 'is':
            return ' '.join(wordList[i+2:])


def searchAbout(text):
    if ('who is' in text):
        thing = getPerson(text)
    else:
        thing = getObject(text)
    try:
        wiki = wikipedia.summary(thing, sentences=2)
        return wiki
    except wikipedia.exceptions.DisambiguationError:
        return "multiple pages found!"
    except wikipedia.exceptions.PageError:
        return "page was not found in wikipedia"
    except wikipedia.exceptions.WikipediaException:
        return "wikipedia server error"
