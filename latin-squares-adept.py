import random

def generateLatinSquare(n):
    square = [[(i + j) % n + 1 for j in range(n)] for i in range(n)]
    return square

def applyFixedFirstRow(square, n):
    square[0] = list(range(1, n + 1))
    return square

def applyNoConsecutiveAdjacent(square, n):
    def isValid(x, y, num):
        if x > 0 and abs(square[x-1][y] - num) == 1:
            return False
        if y > 0 and abs(square[x][y-1] - num) == 1:
            return False
        return True

    for i in range(n):
        for j in range(n):
            num = square[i][j]
            if not isValid(i, j, num):
                for k in range(1, n + 1):
                    if isValid(i, j, k):
                        square[i][j] = k
                        break
    return square

def applyDiagonalUniqueness(square, n):
    diag1 = set()
    diag2 = set()
    for i in range(n):
        diag1.add(square[i][i])
        diag2.add(square[i][n-i-1])
    if len(diag1) != n or len(diag2) != n:
        for i in range(n):
            square[i][i] = (i + 1) % n + 1
            square[i][n-i-1] = (i + 2) % n + 1
    return square

def printSquare(square, n):
    for row in square:
        print(' '.join(str(x) if x <= 9 else chr(x + 55) for x in row))

def main():
    n = int(input("Enter a number N (4 <= N <= 15): "))
    if n < 4 or n > 15:
        print("Invalid input. N must be between 4 and 15.")
        return

    square = generateLatinSquare(n)
    constraint = random.choice(['FixedFirstRow', 'NoConsecutiveAdjacent', 'DiagonalUniqueness'])

    if constraint == 'FixedFirstRow':
        square = applyFixedFirstRow(square, n)
    elif constraint == 'NoConsecutiveAdjacent':
        square = applyNoConsecutiveAdjacent(square, n)
    elif constraint == 'DiagonalUniqueness':
        square = applyDiagonalUniqueness(square, n)

    print(f"Generated Latin Square with constraint: {constraint}")
    printSquare(square, n)

main()