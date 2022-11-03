# 계수 정렬

l = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
r = []
min_value = min(l)
max_value = max(l)

for i in range(min_value, max_value+1):
    cnt = l.count(i)
    for _ in range(cnt):
        r.append(i)
print(*r)