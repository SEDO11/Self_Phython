# 만들 수 없는 금액

n = int(input())
c = list(map(int,input().split()))
c.sort()

target = 1
for i in c:
    if i > target:
        break
    else:
        target+=i
print(target)