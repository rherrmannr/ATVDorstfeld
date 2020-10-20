from datetime import datetime, timedelta, time

HOUR_CHOICES = [(time(hour=x), '{:02d}:00'.format(x)) for x in range(6, 22)]

MY_CHOICES = [
    (datetime(year=2020, month=10, day=20, hour=8), '2020-10-20 8:00'),
    (datetime(year=2020, month=10, day=20, hour=9), '2020-10-20 9:00'),
]

ALL_CHOICES = []
print(HOUR_CHOICES)
print(MY_CHOICES)
current = datetime.now()
ALL_CHOICES.append(
    (datetime(year=current.year, month=current.month, day=current.day, hour=x),
     '{}-{}-{} {:02d}:00'.format(current.year, current.month, current.day, x)) for x in
    range(current.hour + 1, 22))

SOME_CHOICE = [
    (datetime(year=current.year, month=current.month, day=current.day, hour=x),
     '{}-{}-{} {:02d}:00'.format(current.year, current.month, current.day, x)) for x in
    range(current.hour + 1, 22)
]
print(ALL_CHOICES)
for x in range(1, 3):
    current = current + timedelta(days=1)
    print('the future: ' + str(current))
    ALL_CHOICES.append(
        (datetime(year=current.year, month=current.month, day=current.day, hour=x),
         '{}-{}-{} {:02d}:00'.format(current.year, current.month, current.day, x)) for x in
        range(6, 22))

print(ALL_CHOICES)
