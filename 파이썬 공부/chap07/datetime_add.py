from calendar import week
from datetime import *

now = datetime.now()

# 특정 시간 이후의 시간 구하기
# timedelta로 시간 더함
after = now + timedelta(weeks=1, 
    days=1, hours=1, minutes=1, seconds=1) # 1주 1일 1시 1분 1초 더하기
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

output = now.replace(year=(now.year + 1)) # 1년 더하기
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))