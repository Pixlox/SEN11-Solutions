def caesarCipher(message, shift):
    result = []
    for char in message:
        if char.isalpha():
            shiftBase = ord('A') if char.isupper() else ord('a')
            shiftedChar = chr((ord(char) - shiftBase + shift) % 26 + shiftBase)
            result.append(shiftedChar)
        else:
            result.append(char)
    return ''.join(result)

def letterFrequencyAnalysis(encryptedMessage):
    # approx frequencies of each letter in english
    englishFreq = [8, 1.4, 2.7, 4.2, 12, 2.2, 2, 6, 6.9, 0.1, 0.7, 4, 2.4, 6.7, 7.5, 1.9, 0.09, 5.9, 6.3, 9, 2.7, 0.9, 2.3, 0.1, 1.9, 0.07]

    messageFreq = [0] * 26
    for char in encryptedMessage:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')
            messageFreq[index] += 1

    totalLetters = sum(messageFreq)
    messageFreq = [freq / totalLetters * 100 for freq in messageFreq]

    minDiff = float('inf')
    bestShift = 0
    for shift in range(26):
        diff = sum(abs(messageFreq[(i + shift) % 26] - englishFreq[i]) for i in range(26))
        if diff < minDiff:
            minDiff = diff
            bestShift = shift

    return bestShift

def decryptCaesarCipher(encryptedMessage):
    shift = letterFrequencyAnalysis(encryptedMessage)
    return caesarCipher(encryptedMessage, -shift)

encryptedMessage = input("Enter an encrypted message: ")

decryptedMessage = decryptCaesarCipher(encryptedMessage)
print(f"Decrypted message: {decryptedMessage}")