from AI import ai;
from command1 import command as ca;
from main1 import base;

def password():
    attempts=3
    ai.talk("Your personal Assistant is locked, You have only 3 attempts to unlock")
    ai.talk("Start now")
    while attempts>0:
        pwd=ca.take_command()
        if ("open"==pwd):
            ai.talk("You got it correct,Your personal Assistant is unlocked ")
            ai.talk("Hey!I'm SIRI-your personal voice assistant")
            while True:
                base.run_siri()
            return
        else:
            attempts-=1;
            if(attempts==0):
                ai.talk("No attempts REMAIN, Try again Later")
                return
            elif(attempts==1):
                ai.talk("Only one attempt remain,Think before your answer")
            else:
                ai.talk(str(attempts)+" Remains")
                