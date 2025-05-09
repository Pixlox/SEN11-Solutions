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

def decryptCaesarCipher(encryptedMessage):
    possibleMessages = []
    for shift in range(1, 26):
        decryptedMessage = caesarCipher(encryptedMessage, -shift)
        if isLikelyMessage(decryptedMessage):
            possibleMessages.append(decryptedMessage)
    return possibleMessages

def isLikelyMessage(message):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    vowelCount = sum(1 for char in message if char in vowels)
    consonantCount = sum(1 for char in message if char in consonants)
    totalLetters = vowelCount + consonantCount

    if totalLetters == 0 or vowelCount / totalLetters < 0.2:
        return False
    return True

encryptedMessage = input("Enter an encrypted message: ")

possibleMessages = decryptCaesarCipher(encryptedMessage)
print("Possible decrypted messages:")
for msg in possibleMessages:
    print(msg)