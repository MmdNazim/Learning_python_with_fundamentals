import datetime
#working with Date, year, month, day, time, weekDay, hour, minute, second:
"""
current_datetime = datetime.datetime.now()

print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.date())
print(current_datetime.time())
print(current_datetime.weekday())    #[ei function call krle week er kototomo din ta ber kra jay]
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
"""

#datetime formating: yyyy-mm-dd, yyyy-dd-mm, dd-mm-yyyy
"""
current_datetime = datetime.datetime.now()

formated_datetime = current_datetime.strftime("%d-%m-%y  %H:%M:%S")

print(formated_datetime)
"""

#calculating time difference:

date1 = datetime.datetime(2024, 12, 10)
date2 = datetime.datetime(2025, 12, 10)
difference = date2 - date1

print(difference)

new_date = date1 + datetime.timedelta(days = 20)   #[eivabe amra specific date theke days add ba substract krte pari]
print(new_date)