number = int(input("Enter number: "))

if number < 10:
    print("bad input")
else:
    digitSum = 0
    while number > 0:
        digitSum += number % 10
        number //= 10

    print(f"Sum: {digitSum}")