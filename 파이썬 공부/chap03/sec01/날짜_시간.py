import datetime

now = datetime.datetime.now() #지금 현재 날짜 시간 가져오기

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("{}년 {}월 {}일 {}시 {}분 {}초"
      .format(now.year, now.month, now.day,
              now.hour, now.minute, now.second,)) #format 이용