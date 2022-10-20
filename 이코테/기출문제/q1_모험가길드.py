# 모험가 길드
# 공포도

n = input()
l = list(map(int, input().split()))
l.sort()
r = 0
cnt = 1
t = 0
for i in l:
    if i <= cnt:
        t += 1
        cnt = 1
    else:
        cnt += 1
print(t)