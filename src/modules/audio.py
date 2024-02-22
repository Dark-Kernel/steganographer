import os
import wave
import argparse


def help():
  print("\033[92m\nHide Your Secret Message in Audio Wave File.\033[0m")
  print ('''usage:

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File
  -m SECRETMSG  Enter your message
  -o OUTPUTFILE Your output_file file path and name''')
  
def em_audio(audio_file, string_msg, output_file, arged=True):
    if not arged:
      help()
    else:
      print ("Please wait...")
      waveaudio = wave.open(audio_file, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string_msg = string_msg + int((len(frame_bytes)-(len(string_msg)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string_msg])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(f"outdir/{output_file}", 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print ("Done...")

