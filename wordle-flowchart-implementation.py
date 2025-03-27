import random
from wordlist import wordlist

def main():
    word = random.choice(wordlist)
    count = 0
    won = False

    while count < 6 and not won:
        guess = getGuess(wordlist)
        won = checkGuess(guess, word)
        count += 1

    displayMessage(word, won, count)

def getGuess(wordlist):
    valid = False
    while not valid:
        guess = input("Enter your guess: ").lower().strip()
        if len(guess) != 5:
            print("Invalid guess")
            continue

        i = 0
        found = False
        while i < len(wordlist) and not found:
            if guess == wordlist[i]:
                found = True
            i += 1

        if found:
            valid = True
        else:
            print("Invalid guess")

    return guess

def checkGuess(guess, word):
    correct = True
    if guess == word:
        return correct

    correct = False
    for i in range(5):
        if guess[i] == word[i]:
            print(f"{guess[i]} is in the right position")
        elif guess[i] in word:
            print(f"{guess[i]} is in the word but wrong position")
        else:
            print(f"{guess[i]} is not in the word")

    return correct

def displayMessage(word, won, count):
    if won:
        print(f"You guessed the word in {count} guesses!")
    else:
        print(f"You lost. The word was {word}")


main()