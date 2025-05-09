number = input("Enter a number: ")
numberString = str(number)

def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

iterations = 0
max_iterations = 500

while not is_palindrome(numberString):
    if iterations == 50:
        print("Still searching for a palindrome...")
    if iterations >= max_iterations:
        print("This is a potential Lychrel number.")
        break

    reversed_number = int(numberString[::-1])
    number = int(numberString) + reversed_number
    numberString = str(number)
    iterations += 1
else:
    print(f"{number} is a palindrome.")