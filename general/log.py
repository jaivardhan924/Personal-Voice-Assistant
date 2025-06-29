from AI import ai;
from command1 import command as ca;
import os;

def show_log():    
    log_path="C:\\Users\\jaiva\\qandA.txt"
    if os.path.exists(log_path):
        os.system(log_path)
    else:
        ai.talk('File Not found')