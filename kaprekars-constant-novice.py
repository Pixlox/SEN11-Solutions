def kaprekarSteps(number):
    steps = 0
    while number != 6174:
        digits = list(f"{number:04d}")
        ascendingDigits = int(''.join(sorted(digits)))
        descendingDigits = int(''.join(sorted(digits, reverse=True)))
        number = descendingDigits - ascendingDigits
        steps += 1
        print(f"{descendingDigits:04d} - {ascendingDigits:04d} = {number:04d}")
    return steps


number = input("Enter a four-digit integer (at least two digits must be different): ")

if len(number) != 4 or not number.isdigit() or len(set(number)) < 2:
    print("Bad input!")
else:
    number = int(number)
    steps = kaprekarSteps(number)
    print(f"Kaprekar's constant reached in {steps} steps.")
