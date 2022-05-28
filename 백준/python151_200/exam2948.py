#2009년
from datetime import date
def what_day_is_it(date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = date.weekday()
    print(days[day])
d, m = map(int, input().split())
what_day_is_it(date(2009, m, d))
