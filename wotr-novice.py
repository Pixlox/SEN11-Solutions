commonWords = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
]

def readFile(filePath):
    with open(filePath, 'r') as file:
        words = file.read().split()
    return words

def countWords(words):
    wordCount = {}
    for word in words:
        if word not in commonWords:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
    return wordCount

def getMostLeastCommonWords(wordCount, n=5):
    sortedWords = sorted(wordCount.items(), key=lambda item: item[1], reverse=True)
    mostCommon = sortedWords[:n]
    leastCommon = sortedWords[-n:]
    return mostCommon, leastCommon


filePath = 'lotr.txt'
words = readFile(filePath)
wordCount = countWords(words)
mostCommon, leastCommon = getMostLeastCommonWords(wordCount)

print("Five most common words:")
for word, count in mostCommon:
    print(f"{word}: {count}")

print("\nFive least common words:")
for word, count in leastCommon:
    print(f"{word}: {count}")