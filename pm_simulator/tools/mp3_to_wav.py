#!/usr/bin/env python3

import sys
from pydub import AudioSegment


def change_mp3_filename_to_wav(input_file: str):
    return input_file.replace(".mp3", ".wav")


def convert_mp3_to_wav(mp3_file: str, wav_file: str):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")
    print("Convert {} to {}".format(mp3_file, wav_file))


def convert_mp3(mp3_file: str):
    wav_file = change_mp3_filename_to_wav(mp3_file)
    convert_mp3_to_wav(mp3_file, wav_file)


def main():
    #intput_file = "../../voices/change_background_to_red.mp3"
    if len(sys.argv) < 2:
        print("Need mp3 input file as parameter, exit now")
        return
    elif len(sys.argv) == 2:
        convert_mp3(sys.argv[1])
    elif len(sys.argv) == 3:
        convert_mp3_to_wav(sys.argv[1], sys.argv[2])
    else:
        print("Do not support these parameters, exit now")
        return

if __name__ == "__main__":
    main()
