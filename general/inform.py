from AI import ai;
from command1 import command as ca;
import pywhatkit                    #Automates YouTube, WhatsApp, handwriting, etc.
import wikipedia                    #gets topic summaries



def info(command):
    for phrase in ["who is", "tell me about", "give information about", "founder of"]:
            if phrase in command:
                person = command.replace(phrase, "").strip()
                break;
    try:

        info = wikipedia.summary(person, sentences=2)
        ai.talk(info)
        with open("C:\\Users\\jaiva\\qandA.txt","a",encoding="utf-8") as fl:
            fl.write("\nQ)"+command+"\nA)"+info)
    except:
        ai.talk("I didn't found it")