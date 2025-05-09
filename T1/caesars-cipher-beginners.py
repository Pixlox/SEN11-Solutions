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

message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))

encryptedMessage = caesarCipher(message, shift)
print(f"Encrypted message: {encryptedMessage}")