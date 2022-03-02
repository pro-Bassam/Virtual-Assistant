import datetime
import webbrowser as wb
import subprocess

def makeNote(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-")+"-note.txt"
    path = "data/notes/" + file_name

    with open(path, "w") as f:
        f.write(text)
