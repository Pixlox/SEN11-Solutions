number = input("Enter a number: ")
numberString = str(number)

isPalindrome = True
length = len(numberString)

for i in range(length // 2):
    if numberString[i] != numberString[length - i - 1]:
        isPalindrome = False
        break

if isPalindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")