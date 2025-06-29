from AI import ai;
from command1 import command as ca;

def clear():        
    log_path="C:\\Users\\jaiva\\qandA.txt"
    with open(log_path,'w',encoding='utf-8') as f:
        f.write("")
    ai.talk("Log Cleared")