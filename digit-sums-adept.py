def sumOfDigits(number):
    digitSum = 0
    while number > 0:
        digitSum += number % 10
        number //= 10
    return digitSum

numberInput = int(input("Enter number: "))

if numberInput < 10:
    maxDigitSum = numberInput
else:
    strNumberInput = str(numberInput)
    length = len(strNumberInput)
    candidate = int('9' * (length - 1))

    if candidate > numberInput:
        candidate = int('9' * (length - 2))

    if sumOfDigits(numberInput) >= sumOfDigits(candidate):
        maxDigitSum = numberInput
    else:
        maxDigitSum = candidate

print(f"The number <= {numberInput} with the greatest digit sum is: {maxDigitSum}")