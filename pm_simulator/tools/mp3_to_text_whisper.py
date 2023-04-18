#!/usr/bin/env python3

import sys
import whisper


def mp3_to_text(mp3_file: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(mp3_file)
    print("Convert mp3 file {} to text: {}".format(mp3_file, result["text"]))
    # Take almost 1.44 seconds to run
    

def main():
    #mp3_file = "../output.mp3"
    mp3_file = sys.argv[1]
    mp3_to_text(mp3_file)


if __name__ == "__main__":
    main()
