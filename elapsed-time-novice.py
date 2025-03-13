from datetime import datetime, timedelta

def getTimezoneDifference(offset1, offset2):
    offset1 = timedelta(hours=int(offset1))
    offset2 = timedelta(hours=int(offset2))

    difference = (offset2 - offset1).total_seconds() / 3600
    return difference


timezonesInput = input("Enter two timezone offsets separated by a comma in UTC (e.g., '-5,1'): ")
offset1, offset2 = [tz.strip() for tz in timezonesInput.split(',')]

try:
    difference = getTimezoneDifference(offset1, offset2)
    print(f"The difference between the timezones is {difference} hours.")
except Exception as e:
    print(f"Bad input likely, error: {e}")