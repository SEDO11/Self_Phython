from datetime import *

now = datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

out_a = now.strftime("%Y.%m.%d %H:%M:%S")

print(out_a)