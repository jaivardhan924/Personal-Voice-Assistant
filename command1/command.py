from AI import ai

import speech_recognition as sr     #to recognise the voice(speech to text)


def take_command():
    listener = sr.Recognizer()          #recognizing and processing speech from the microphone
    with sr.Microphone() as source:     #open microphone uses it as an input audio source.
        print("Listening...")    
        listener.adjust_for_ambient_noise(source)   #Helps reduce background noise by calibrating the recognizer to ignore it
        voice = listener.listen(source)             #Records audio from the microphone and saves it in the voice variable
    try:
        command = listener.recognize_google(voice)  #Sends the recorded audio to Google's speech recognition API and gets back a string
        command = command.lower()                   #covert the command into small letters
        print("You said:", command)
    except sr.UnknownValueError:
        ai.talk("Sorry , I didn’t catch that.")
        return ""
    except sr.RequestError:
        ai.talk("Network issue with Google service.")
        return ""
    return command