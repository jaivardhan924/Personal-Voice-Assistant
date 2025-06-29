
import pyttsx3


def talk(text):
    # Initialize speech engine
    a = pyttsx3.init()
    a.setProperty('rate', 170)          # number of words per minute(default= 200 words)
    volume = a.getProperty('volume')
    a.setProperty('volume',0.8)         #volume upto 80%
    voices = a.getProperty('voices')
    a.setProperty('voice', voices[0].id)         # 0-> male voice,1-> female voice

    print("SIRI:", text)
    a.say(text)
    a.runAndWait()