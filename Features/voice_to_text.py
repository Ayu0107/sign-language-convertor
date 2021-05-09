import speech_recognition as sr
#install speechrecognition and pyaudio packages
listen =sr.Recognizer()
try:
    with sr.Microphone() as source:
        voice = listen.listen(source)
        c = listen.recognize_google(voice)
        print("listening....")
        c=c.lower()
        print(c)
except:
    pass