#2007년
from datetime import date
def what_day_is_it(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    print(days[day])
m, d = map(int, input().split())
what_day_is_it(date(2007, m, d))
