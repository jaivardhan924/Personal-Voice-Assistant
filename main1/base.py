from AI import ai;
from command1 import command as ca;

from general import yout;
from general import time as a_time;
from general import myself as ms;
from general import inform as im;
from general import log;
from general import clear;
from general import joke;
from general import chrome;
from general import coding;

from camera import resize as r;
from camera import picture as p; 
from camera import capture as c;

from main1 import main;


import pyttsx3
import pywhatkit                    #Automates YouTube, WhatsApp, handwriting, etc.
import speech_recognition as sr     #to recognise the voice(speech to text)
import wikipedia                    #gets topic summaries   
import pyjokes                      #Adds humor with jokes
import os
import sys
import time;
import datetime;

def run_siri():
    time1 = datetime.datetime.now()
    command = ca.take_command()
    

    if "play" in command:
        yout.yt(command)
       
    elif "what's the time" in command:
        a_time.time();

    elif "who is Jai vardhan" in command:
        ms.me();

    elif any(phrase in command for phrase in ["who is", "tell me about", "give information about", "founder of"]):
        im.info(command);    

    elif "show log" in command or "log info" in command:
        log.show_log();
        
    elif "clear log" in command or "close log" in command:
        ai.talk("Are you sure you want to clear the log?")
        confirm_clear = ca.take_command().lower()

        if "yes" in confirm_clear:
            clear.clear()
            ai.talk("Log cleared.")
        else:
            ai.talk("Log not cleared.")
    elif "joke" in command:
        joke.joke();

    elif "open chrome" in command:
        chrome.chrome();

    elif "open code" in command or "open vs code" in command:
        coding.coding();

    elif "open camera" in command:
        ai.talk("Opening Camera for a live video")
        ai.talk("press q to quit")
        c.came()

    elif "take a pic" in command or "take picture" in command:
        ai.talk("Press 's' to Capture your moment")
        name="";
        while not name:
            ai.talk("Please say a name to save your file")
            name=ca.take_command();
            if name:
                ai.talk("you got a file name")
            else:
                ai.talk("I couldn't here you, Say it Loudly")
        file_name=name.replace(' ','_')+".jpg";
        ai.talk("Do you want me to save this photo? Say 'yes' or 'no'")
        con = ca.take_command().lower()

        if "yes" in con:
            p.pic(file_name)
            ai.talk("Photo saved successfully.")
        else:
            ai.talk("Okay, not saving the photo.")

    elif "lock the assistant" in command or "lock" in command:
        main.password();  

    elif "thank you" in command:
        ai.talk("You are always welcome")

    elif "show screen time" in command:
        time2=datetime.datetime.now()
        tim=time2-time1
        ai.talk("your screen time is "+str(tim))

    elif "e n d" in command or "close" in command:
        ai.talk("Okay , see you later")
        sys.exit()

    elif command != "":
        ai.talk("I heard you, but I don’t understand that yet")