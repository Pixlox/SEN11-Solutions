def kaprekarSteps(number):
    steps = 0
    while number != 495:
        digits = list(f"{number:03d}")
        ascendingDigits = int(''.join(sorted(digits)))
        descendingDigits = int(''.join(sorted(digits, reverse=True)))
        number = descendingDigits - ascendingDigits
        steps += 1
        print(f"{descendingDigits:03d} - {ascendingDigits:03d} = {number:03d}")
    return steps


number = input("Enter a three-digit integer (at least two digits must be different): ")

if len(number) != 3 or not number.isdigit() or len(set(number)) < 2:
    print("Bad input!")
else:
    number = int(number)
    steps = kaprekarSteps(number)
    print(f"Kaprekar's constant for three-digit numbers reached in {steps} steps.")