#this code is to convert the text to voice on the spot and to listen
import speech_recognition as sr
import pyttsx3

listen = sr.Recognizer()
try:
    with sr.Microphone() as source:
        voice = listen.listen(source)
        c = listen.recognize_google(voice)
        print("listening....")
        c=c.lower()
        print(c)
except:
    pass

speaker=pyttsx3.init()
speaker.say(c)
speaker.runAndWait()