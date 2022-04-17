# 지능형 기차 2

result = 0
max_r = 0
for _ in range(10):
    o, i = map(int, input().split())
    result += i - o
    max_r = max(max_r, result)
print(max_r)