def isLatinSquare(grid):
    n = len(grid)
    validSet = set(range(1, n + 1))

    # row check
    for i, row in enumerate(grid):
        if set(x for x in row if x != 0) != validSet:
            return False, f"Row {i + 1} is invalid"

    # col check
    for col in range(n):
        column = [grid[row][col] for row in range(n)]
        if set(x for x in column if x != 0) != validSet:
            return False, f"Column {col + 1} is invalid"

    return True, "The grid is a Latin Square"

def isValid(grid, row, col, num):
    n = len(grid)
    for x in range(n):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    return True

def solveLatinSquare(grid):
    n = len(grid)
    for row in range(n):
        for col in range(n):
            if grid[row][col] == 0:
                for num in range(1, n + 1):
                    if isValid(grid, row, col, num):
                        grid[row][col] = num
                        if solveLatinSquare(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

print("Please enter your grid, with each character separated by a space and each row on a new line, with blank cells represented by an underscore: ")

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

# convert letters to int if any (kinda bugged sometimes though)
charToInt = {}
currentInt = 1
for i in range(n):
    for j in range(n):
        if userInput[i][j] == '_':
            userInput[i][j] = 0
        else:
            if userInput[i][j] not in charToInt:
                charToInt[userInput[i][j]] = currentInt
                currentInt += 1
            userInput[i][j] = charToInt[userInput[i][j]]

if solveLatinSquare(userInput):
    print("One possible solution to the given puzzle is:")
    for row in userInput:
        print(' '.join(str(x) for x in row))
else:
    print("No solution exists for the square :(")