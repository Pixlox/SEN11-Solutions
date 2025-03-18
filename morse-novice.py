import time
import os
import wave
import struct
import tempfile

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def generateToneFile(filename, duration, frequency=800):
    sampleRate = 44100
    amplitude = 32767
    numSamples = int(duration * sampleRate)

    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, sampleRate, 0, 'NONE', 'not compressed'))
        # Generate samples
        samples = []
        for i in range(numSamples):
            sample = amplitude * struct.pack('h', int(amplitude * (i * frequency / sampleRate % 1 * 2 - 1)))
            samples.append(sample[0:2])

        wav_file.writeframes(b''.join(samples))

# tempdir and wav files
tempDir = tempfile.mkdtemp()
dotFile = os.path.join(tempDir, "dot.wav")
dashFile = os.path.join(tempDir, "dash.wav")

# Generate the audio files
generateToneFile(dotFile, 0.2)  # 0.2s works
generateToneFile(dashFile, 0.6)

def play_sound(sound_type):
    if sound_type == '.':  # dot
        os.system(f"afplay {dotFile}")
        time.sleep(0.1)  # gap between symbols
    elif sound_type == '-':  # dash
        os.system(f"afplay {dashFile}")
        time.sleep(0.1)  # gap between symbols
    elif sound_type == ' ':  # space between letters
        time.sleep(0.3)
    elif sound_type == '/':  # space between words
        time.sleep(0.7)

def play_morse_code(morse_text):
    print("Playing morse code...")
    for symbol in morse_text:
        play_sound(symbol)
        print(symbol, end='', flush=True)
    print("\nDone playing.")

def string_to_morse():
    user_input = input("Enter a string: ").upper()
    morse_code = ""

    for char in user_input:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        elif char == " ":
            morse_code += "/ "

    print(f"Morse code: {morse_code}")
    play_morse_code(morse_code)
    return morse_code



try:
    string_to_morse()
finally:
    # i am extremely sorry for bloating your drive :(
    if os.path.exists(dotFile):
        os.remove(dotFile)
    if os.path.exists(dashFile):
        os.remove(dashFile)
    if os.path.exists(tempDir):
        os.rmdir(tempDir)