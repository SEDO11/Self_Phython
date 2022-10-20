#만들 수 없는 금액

n = int(input())
l = list(map(int, input().split()))
l.sort()
r = 1
for i in l:
    if i <= r:
        r += i
    else:
        break
print(r)