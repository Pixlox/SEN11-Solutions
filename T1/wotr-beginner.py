def readFile(filePath):
    with open(filePath, 'r') as file:
        words = file.read().split()
    return list(set(words))

filePath = 'lotr.txt'
words = readFile(filePath)

userWord = input("Enter a word to search: ").strip()
if userWord in words:
    print(f"The word '{userWord}' appears in the text")
else:
    print(f"The word '{userWord}' does not appear in the text")
