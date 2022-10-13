# 모험가 공포도

n = list(map(int, input().split()))
n.sort()
r = 0
cnt = 0
for i in n:
    r += 1
    if i <= r:
        cnt += 1
        r = 0
print(cnt)