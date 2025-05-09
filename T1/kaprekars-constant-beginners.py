number = input("Enter a four-digit integer (at least two digits must be different): ")


digits = list(number)
ascendingDigits = ''.join(sorted(digits))
descendingDigits = ''.join(sorted(digits, reverse=True))

print(f"Ascending - {ascendingDigits}")
print(f"Descending - {descendingDigits}")