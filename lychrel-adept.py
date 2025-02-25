def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

def find_palindrome(numberString, iterations, max_iterations):
    if is_palindrome(numberString):
        return numberString, iterations
    if iterations >= max_iterations:
        return None, iterations

    reversed_number = int(numberString[::-1])
    number = int(numberString) + reversed_number
    return find_palindrome(str(number), iterations + 1, max_iterations)

max_iterations = 500
max_iterations_number = 0
max_iterations_count = 0
palindrome_result = ""

for num in range(1, 20001):
    numberString = str(num)
    result, iterations = find_palindrome(numberString, 0, max_iterations)

    if result and iterations > max_iterations_count:
        max_iterations_count = iterations
        max_iterations_number = num
        palindrome_result = result

print(f"The number {max_iterations_number} took the most iterations ({max_iterations_count}) to become a palindrome: {palindrome_result}.")