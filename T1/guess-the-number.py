import random
import json
import time

def main():
    randInt = random.randint(1, 100)
    guesses = 0
    start_time = time.time()

    print("Input a number between 1 and 100.")

    try:
        with open("highScore.json", "r") as file:
            high_scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        high_scores = []

    while True:
        try:
            guess = int(input())
            guesses += 1
            if guess < randInt:
                print("Higher")
            elif guess > randInt:
                print("Lower")
            else:
                end_time = time.time()
                time_taken = end_time - start_time
                score = guesses + (time_taken / 100)  # Weight guesses higher than time
                print(f"Correct! You guessed the number in {guesses} guesses and {time_taken:.2f} seconds!")
                print(f"Your score is {score:.2f}")

                if len(high_scores) < 3 or score < high_scores[-1]['score']:
                    name = input("New high score! Enter your name: ")
                    high_scores.append({'name': name, 'score': score})
                    high_scores = sorted(high_scores, key=lambda x: x['score'])[:3]
                    with open("highScore.json", "w") as file:
                        json.dump(high_scores, file, indent=4)
                    print("High scores updated!")

                break
        except ValueError:
            print("Invalid input.")

main()