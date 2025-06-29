from AI import ai;
from command1 import command as ca;
import pyjokes;


def joke():
    ai.talk(pyjokes.get_joke(language='en', category='neutral'))
    with open("C:\\Users\\jaiva\\qandA.txt","a",encoding="utf-8") as fl:
        fl.write("\nJokes :"+pyjokes.get_joke(language='en', category='neutral'))