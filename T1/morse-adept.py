from pydub import AudioSegment

morseCodeDict = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',
    '.': 'E',     '..-.': 'F',  '--.': 'G',   '....': 'H',
    '..': 'I',    '.---': 'J',  '-.-': 'K',   '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',   '.--.': 'P',
    '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',
    '-.--': 'Y',  '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

def audioToBinary(audio, threshold):
    binary = []
    for ms in range(len(audio)):
        segment = audio[ms:ms+1]
        if segment.rms > threshold:
            binary.append(1)
        else:
            binary.append(0)
    return binary

def groupBinary(binary):
    groups = []
    if not binary:
        return groups
    currentVal = binary[0]
    count = 0
    for bit in binary:
        if bit == currentVal:
            count += 1
        else:
            groups.append((currentVal, count))
            currentVal = bit
            count = 1
    groups.append((currentVal, count))
    return groups

def decodeGroups(groups, ditDuration):
    morseCode = ""
    dahDuration = ditDuration * 3
    toneMidpoint = (ditDuration + dahDuration) / 2

    for value, duration in groups:
        if value == 1:
            if duration < toneMidpoint:
                morseCode += '.'
            else:
                morseCode += '-'
        else:
            if duration < ditDuration * 2:
                pass
            elif duration < ditDuration * 4:
                morseCode += ' '
            else:
                morseCode += '   '
    return morseCode

def morseToText(morseCode):
    decodedWords = []
    for word in morseCode.split("   "):
        letters = word.split()
        decodedLetters = [morseCodeDict.get(letter, '?') for letter in letters]
        decodedWords.append("".join(decodedLetters))
    return " ".join(decodedWords)

filePath = input("Where is the file located? : ")
dit_duration = 100

audio = AudioSegment.from_file(filePath, format="wav")
threshold = audio.max * 0.1

binary = audioToBinary(audio, threshold)
groups = groupBinary(binary)
morseCode = decodeGroups(groups, dit_duration)
englishMessage = morseToText(morseCode)

print("Morse Code:", morseCode)
print("English Message:", englishMessage)