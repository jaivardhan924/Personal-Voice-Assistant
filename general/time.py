from AI import ai;
from command1 import command as ca;
import datetime                     #to access the date,time,year


def time():        
    time = datetime.datetime.now().strftime('%I:%M %p')
    ai.talk("It is "+time)
    with open("C:\\Users\\jaiva\\qandA.txt","a",encoding="utf-8") as fl:
        fl.write("\nTime is :"+time)