import datetime

# a string
mikes_dob = "Dec 6, 1970"
mikes_dob_date = datetime.datetime.strptime(mikes_dob, "%b %d, %Y").date()
four_weeks = datetime.timedelta(weeks=4)
four_weeks_from_dob = mikes_dob_date + four_weeks
mike_dob_dow = mikes_dob_date.strftime("%A")


# python datetime object
today = datetime.date.today()

print(f"Today is {today}")
print(f"Mike's date of birth is {mikes_dob_date}")
print(f"Four weeks from Mike's date of birth is {four_weeks_from_dob}")
print(f"Mike's date of birth was on a {mike_dob_dow}")

'''
January 12, 2027

2023-12-01T14:30:01

'''
# strptime for the last two examples
january_12_2027 = "January 12, 2027"
january_12_2027_date = datetime.datetime.strptime(january_12_2027, "%B %d, %Y").date()
iso_2023_12_01 = "2023-12-01T14:30:01"
iso_2023_12_01_date = datetime.datetime.strptime(iso_2023_12_01, "%Y-%m-%dT%H:%M:%S").date()

print(f"January 12, 2027 as a date object is {january_12_2027_date}")
print(f"ISO 2023-12-01T14:30:01 as a date object is {iso_2023_12_01_date}") 