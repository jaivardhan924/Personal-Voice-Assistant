from AI import ai;
from command1 import command as ca;
import pywhatkit;

def yt(comm):
    song = comm.replace("play", "")
    ai.talk("Playing on YouTube")
    pywhatkit.playonyt(song)
    with open("C:\\Users\\jaiva\\qandA.txt","a",encoding="utf-8") as fl:
        fl.write("\nThe Selected song is:"+song)