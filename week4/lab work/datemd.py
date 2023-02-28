import datetime
from datetime import timedelta, datetime
#1
d = datetime.today() - timedelta(days = 5)
print(d)

#2
yesterday = datetime.today() - timedelta(1)
today = datetime.today()
tomorrow = datetime.today() + timedelta(1)
print(yesterday)
print(today)
print(tomorrow)

#3
without_microseconds = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(without_microseconds)

#4
d1 = datetime.strptime('2019-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
d2 = datetime.today()
timedelta = d2 - d1
print(timedelta.days * 24 * 3600 * timedelta.seconds)