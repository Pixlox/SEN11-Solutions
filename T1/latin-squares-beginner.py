def isLatinSquare(grid):
    n = len(grid)
    valid_set = set(range(1, n + 1))

    # rows check
    for i, row in enumerate(grid):
        if set(row) != valid_set:
            return False, f"Row {i + 1} is invalid"

    # col check
    for col in range(n):
        column = [grid[row][col] for row in range(n)]
        if set(column) != valid_set:
            return False, f"Column {col + 1} is invalid"

    return True, "The grid is a Latin Square"

print("Please enter your grid, with each character separated by a space and each row on a new line: ")

userInput = []
while True:
    try:
        line = input()
        if line.strip() == "":
            break
        userInput.append(line.split())
    except ValueError:
        print("Bad input. Numbers and letters only.")
        exit()

n = len(userInput)
if any(len(row) != n for row in userInput):
    print("The number of rows and columns are not equal, try again")
    exit()

# convert letters to int if any
charToInt = {}
currentInt = 1
for i in range(n):
    for j in range(n):
        if userInput[i][j] not in charToInt:
            charToInt[userInput[i][j]] = currentInt
            currentInt += 1
        userInput[i][j] = charToInt[userInput[i][j]]

isValid, message = isLatinSquare(userInput)
print(message)