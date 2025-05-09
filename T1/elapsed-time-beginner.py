from datetime import datetime

def validateDate(dateText):
    try:
        return datetime.strptime(dateText, '%d/%m/%Y')
    except ValueError:
        raise ValueError("Bad input, needs to be DD/MM/YYYY")

def calculateAge(birthDate):
    today = datetime.now()
    age = today - birthDate
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    return years, months, days


birthDateInput = input("Enter your birthday (DD/MM/YYYY): ")
birthDate = validateDate(birthDateInput)
years, months, days = calculateAge(birthDate)
print(f"Your age is {years} years, {months} months, and {days} days.")