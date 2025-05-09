number = input("Enter number: ")

if len(number) < 2 or not number.isdigit():
    print("bad input")
else:
    print(f"Sum: {sum(int(digit) for digit in number)}")