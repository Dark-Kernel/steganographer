import os.path
import io

import numpy as np
from scipy.io import wavfile

def phase_encode(pathToAudio,stringToEncode):
    print("Inside phase_encode function")
    rate,audioData1 = wavfile.read(pathToAudio)
    
    stringToEncode = stringToEncode.ljust(100, '~')
    textLength = 8 * len(stringToEncode)
    print(rate)
    chunkSize = int(2 * 2 ** np.ceil(np.log2(2 * textLength)))
    numberOfChunks = int(np.ceil(audioData1.shape[0] / chunkSize))
    audioData = audioData1.copy()
  
    #Breaking the Audio into chunks
    if len(audioData1.shape) == 1:
        audioData.resize(numberOfChunks * chunkSize, refcheck=False)
        audioData = audioData[np.newaxis]
    else:
        audioData.resize((numberOfChunks * chunkSize, audioData.shape[1]), refcheck=False)
        audioData = audioData.T
  
    chunks = audioData[0].reshape((numberOfChunks, chunkSize))
  
    #Applying DFT on audio chunks
    chunks = np.fft.fft(chunks)
    magnitudes = np.abs(chunks)
    phases = np.angle(chunks)
    phaseDiff = np.diff(phases, axis=0)
    
    # Convert message to encode into binary
    textInBinary = np.ravel([[int(y) for y in format(ord(x), "08b")] for x in stringToEncode])
    
    # Convert message in binary to phase differences
    textInPi = textInBinary.copy()
    textInPi[textInPi == 0] = -1
    textInPi = textInPi * -np.pi / 2

    midChunk = chunkSize // 2

    # Phase conversion
    phases[0, midChunk - textLength: midChunk] = textInPi
    phases[0, midChunk + 1: midChunk + 1 + textLength] = -textInPi[::-1]

    # Compute the phase matrix
    for i in range(1, len(phases)):
        phases[i] = phases[i - 1] + phaseDiff[i - 1]
        
    # Apply Inverse fourier trnasform after applying phase differences
    chunks = (magnitudes * np.exp(1j * phases))
    chunks = np.fft.ifft(chunks).real

        # Combining all block of audio again
    audioData[0] = chunks.ravel().astype(np.int16)    

    dir = os.path.dirname("../../outdir")
    print(dir)
    """ avcontent = io.BytesIO()
    wavfile.write(wavcontent, rate, audioData.T) """
    wavfile.write("phase-output.wav", rate, audioData.T)
    """ wavcontent.seek(0)
    wav_data = wavcontent.read() """
    return dir + "/phase-output.wav"

def phase_decode(audioLocation):
    rate, audioData = wavfile.read(audioLocation)
    print(rate)
    textLength = 800
    blockLength = 2 * int(2 ** np.ceil(np.log2(2 * textLength)))
    blockMid = blockLength // 2
    print(blockLength, blockMid)
    # Get header info
    if len(audioData.shape) == 1:
        code = audioData[:blockLength]
    else:
        code = audioData[:blockLength, 0]
    print(code)
    # Get the phase and convert it to binary
    codePhases = np.angle(np.fft.fft(code))[blockMid - textLength:blockMid]
    codeInBinary = (codePhases < 0).astype(np.int16)

    # Convert into characters
    codeInIntCode = codeInBinary.reshape((-1, 8)).dot(1 << np.arange(8 - 1, -1, -1))
    
    # Combine characters to original text
    return "".join(np.char.mod("%c", codeInIntCode)).replace("~", "")

    

