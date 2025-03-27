import random
import curses
from wordlist import wordlist

def main(stdscr):
    curses.curs_set(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK) # looks bad on mac i hope it works on win
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()

    selectedWord = random.choice(wordlist)
    attemptCount = 0
    isWon = False
    maxY, maxX = stdscr.getmaxyx()

    while attemptCount < 6 and not isWon:
        guess = getGuess(stdscr, wordlist, maxY)
        isWon, colors = checkGuess(guess, selectedWord)
        displayGuess(stdscr, guess, colors, attemptCount, maxY)
        attemptCount += 1

    displayMessage(stdscr, selectedWord, isWon, attemptCount)

def getGuess(stdscr, wordlist, maxY):
    promptLine = maxY - 2
    errorLine = maxY - 1

    while True:
        stdscr.move(promptLine, 0)
        stdscr.clrtoeol()
        stdscr.addstr(promptLine, 0, "Enter your guess: ")
        stdscr.refresh()
        curses.echo()

        guess = ""

        try:

            guess = stdscr.getstr(promptLine, len("Enter your guess: "), 5).decode('utf-8').lower().strip()
        except curses.error:
            pass
        curses.noecho()

        if len(guess) != 5:
            stdscr.addstr(errorLine, 0, "Guess must be 5 letters. Press any key.")
            stdscr.getch()
            stdscr.move(errorLine, 0)
            stdscr.clrtoeol()
            continue

        if guess in wordlist:
            break
        else:
            stdscr.addstr(errorLine, 0, "Guess not in word list. Press any key.")
            stdscr.getch()
            stdscr.move(errorLine, 0)
            stdscr.clrtoeol()
    return guess

def checkGuess(guess, selectedWord):
    if guess == selectedWord:
        return (True, [1] * 5)

    colors = []
    wordLetters = list(selectedWord)

    for i in range(5):
        if guess[i] == selectedWord[i]:
            colors.append(1)
            wordLetters[i] = None
        else:
            colors.append(0)

    for i in range(5):
        if colors[i] == 0:
            if guess[i] in wordLetters:
                colors[i] = 2
                wordLetters[wordLetters.index(guess[i])] = None
            else:
                colors[i] = 3
    return (False, colors)

def displayGuess(stdscr, guess, colors, row, maxY):
    startRow = maxY - 8 - (6 - row) * 2
    for i in range(5):
        if startRow >= 0:
            stdscr.addstr(startRow, i * 2, guess[i].upper(), curses.color_pair(colors[i]))
    stdscr.refresh()

def displayMessage(stdscr, selectedWord, isWon, attemptCount):
    stdscr.clear()
    if isWon:
        msg = f"You guessed the word in {attemptCount} guesses!"
    else:
        msg = f"You lost. The word was {selectedWord.upper()}"
    stdscr.addstr(0, 0, msg)
    stdscr.addstr(2, 0, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)
