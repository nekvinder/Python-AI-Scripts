import pyttsx3
import win32com
import winsound

def aprint(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

