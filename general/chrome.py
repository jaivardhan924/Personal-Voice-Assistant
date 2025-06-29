from AI import ai;
from command1 import command as ca;
import pywhatkit;
import os;

def chrome():
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.exists(chrome_path):
        ai.talk("Opening Chrome 🚀")
        os.startfile(chrome_path)
    else:
        ai.talk("Chrome path not found ")