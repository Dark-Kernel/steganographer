import os
import io
import sys
import zlib
import json
import logging
import argparse
import time

from src.modules import audio
from src.modules.help import banner

def main():
    
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()
        
        # Argument parser
        #parser = argparse.ArgumentParser(description="Steganographer is a steganography tool that does everything what it should.")

        parser = argparse.ArgumentParser()
        parser.add_argument('-e', help="Extract the message", action='store_true', dest='extract')
        parser.add_argument('-f', help='Select Audio File', dest='audiofile')
        parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
        parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
        args = parser.parse_args()
        audio_file = args.audiofile
        string_msg = args.secretmsg
        output_file = args.outputfile
        arged = False
        # action = args.extract
    
        if audio_file and string_msg and output_file:
            arged = True

        print("out: ", args.extract)

        if args.extract:
            audio.ex_msg(audio_file, output_file, arged=True)
        else: 
            audio.em_audio(audio_file, string_msg, output_file, arged)
    except Exception as e:
        print ("Something went wrong!! try again", e)
        quit('')

if __name__ == '__main__':
    main()
