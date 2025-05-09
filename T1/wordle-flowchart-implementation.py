import random
from wordlist import wordlist

def main():
    word = random.choice(wordlist)
    print(word)
    count = 0
    won = False

    while count < 6 and not won:
        guess = getGuess()
        count += 1
        won = check(guess, word)

    displayMessage(word, won, count)

def getGuess():
    valid = False
    while not valid:
        guess = input("Enter your guess: ").lower().strip()
        i = 0
        
        while i < len(wordlist):
            if guess == wordlist[i]:
                valid = True
                i = len(wordlist)
            i += 1

        if not valid:
            print("Invalid guess")

    return guess


def check(guess, word):
    correct = False

    if guess == word:
        correct = True
    else:
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                if guess[i] == word[j]:
                    if i == j:
                        print(f"{guess[i]} is in the right position")
                    else:
                        print(f"{guess[i]} is in the wrong position")
                j += 1
            i += 1

    return correct

def displayMessage(word, won, count):
    if won:
        print(f"You guessed the word in {count} guesses!")
    else:
        print(f"You lost. The word was {word}")


main()