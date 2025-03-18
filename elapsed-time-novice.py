import pytz
from datetime import datetime

def getTimezoneDifference(tz1, tz2):
    now = datetime.now()
    timezone1 = pytz.timezone(tz1)
    timezone2 = pytz.timezone(tz2)

    offset1 = timezone1.utcoffset(now)
    offset2 = timezone2.utcoffset(now)

    difference = (offset2 - offset1).total_seconds() / 3600
    return difference

timezonesInput = input("Please enter two timezones separated by a comma (e.g., 'Australia/Sydney,Asia/Tokyo'): ")
tz1, tz2 = [tz.strip() for tz in timezonesInput.split(',')]

try:
    difference = getTimezoneDifference(tz1, tz2)
    print(f"The difference between the timezones is {difference} hours.")
except Exception as e:
    print(f"Bad input likely, error: {e}")