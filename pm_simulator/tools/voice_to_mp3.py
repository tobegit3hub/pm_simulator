#!/usr/bin/env python3

import speech_recognition as sr
import os
from os import path
from gtts import gTTS


# create a speech recognition object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using the Google Speech Recognition API
try:
    text = r.recognize_google(audio)
    print("You said: " + text)

    # convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    print("Save the voice in {}".format("output.mp3"))
    os.system("afplay output.mp3")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
