#!/usr/bin/env python3

import speech_recognition as sr
from os import path
from gtts import gTTS
import sys
import whisper

import client


def mp3_to_text(mp3_file: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(mp3_file)
    text = result["text"]
    print("Read mp3 file {} to text: {}".format(mp3_file, text))
    return text

def wav_to_text(wav_file: str) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print("Read wav file {} to text: {}".format(text))
        return text
    except Exception as e:
        raise Exception("Fail to load wav file: {}, exception: {}, try again if exception is null".format(wav_file, e))


def get_voice_input() -> str:    
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
        print("Save to output.mp3")
        tts.save("output.mp3")
        #os.system("afplay output.mp3")

        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def main():
    if len(sys.argv) > 1:
        voice_file = sys.argv[1]
        if voice_file.endswith(".mp3"):
            command = mp3_to_text(voice_file)
        elif voice_file.endswith(".wav"):
            command = wav_to_text(voice_file)
        else:
            raise Exception("Unsupported file type: {}".format(voice_file))
    else:
        command = get_voice_input()

    client.request_change_css(command)

    
if __name__ == "__main__":
    main()