#!/usr/bin/env python3

import sys
import speech_recognition as sr


def wav_to_text(wav_file: str) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print("Convert {} to text: {}".format(wav_file, text))
        return text
    except Exception as e:
        print("Exception: "+str(e))


def main():
    #input_file = "../../voices/change_background_to_light_yellow.wav"
    input_file = sys.argv[1]
    wav_to_text(input_file)


if __name__ == "__main__":
    main()