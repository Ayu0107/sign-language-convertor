#this code is to convert the text to voice and save the file
from gtts import gTTS
import os
import speech_recognition as sr

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

mytext = c

language ='en'
output = gTTS(text=mytext,lang=language, slow= False)

output.save("output.mp3")

os.system("start output.mp3")