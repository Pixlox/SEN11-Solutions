import random

def readFile(filePath):
    with open(filePath, 'r') as file:
        words = file.read().split()
    return words

def buildWordDict(words):
    wordDict = {}
    for i in range(len(words) - 1):
        word = words[i]
        nextWord = words[i + 1]
        if word not in wordDict:
            wordDict[word] = {}
        if nextWord not in wordDict[word]:
            wordDict[word][nextWord] = 0
        wordDict[word][nextWord] += 1
    return wordDict

def weightedChoice(wordDict):
    total = sum(wordDict.values())
    randVal = random.uniform(0, total)
    cumulative = 0
    for word, weight in wordDict.items():
        cumulative += weight
        if randVal < cumulative:
            return word

def generateSentence(wordDict, startWord, length=10):
    currentWord = startWord
    sentence = [currentWord]
    for _ in range(length - 1):
        if currentWord in wordDict:
            nextWord = weightedChoice(wordDict[currentWord])
            sentence.append(nextWord)
            currentWord = nextWord
        else:
            break
    return ' '.join(sentence)


filePath = 'lotr.txt'
words = readFile(filePath)
wordDict = buildWordDict(words)

startWord = input("Enter a starting word: ").strip()
sentence = generateSentence(wordDict, startWord)
print("Generated sentence:")
print(sentence)