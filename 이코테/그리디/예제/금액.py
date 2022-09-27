# 금액

n = list(map(int, input().split()))
n.sort()
t = 1
for i in n:
    if i > t:
        break
    else:
        t += i
print(t)