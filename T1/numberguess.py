import random

number = random.randint(1, 100)
guess = 0

print(number)
print("Guess the number")

while True:
    try:
        guessNum = int(input("Choose a random number between 1 and 100: "))
        guess += 1

        if guessNum > number:
            print("Your guess is too high")
        elif guessNum < number:
            print("Your guess is too low")
        else:
            print(f"Correct! You guessed the number in {guess} tries.")
            break
    except ValueError:
        print("Invalid number.")


scoreFile = "highScore.txt"

scoreFileasPath = open(scoreFile, "r")

try:
    if scoreFileasPath != "":
        if scoreFileasPath.read().isdigit:
            highscore = int(scoreFileasPath.read())
        else:
            highscore = None
    else:
        highscore = None
except(FileNotFoundError, ValueError):
    highscore = None

if highscore is None or guess < highscore:
    with open(scoreFile, "w") as file:
        file.write(str(guess))
    print(f"New high score! {guess} guesses!!!")
else:
    print(f"Your score is {guess} guesses. High score is {highscore} guesses.")


