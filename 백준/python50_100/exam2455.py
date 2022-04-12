#지능형 기차

result = 0
max_r = 0
for k in range(4):
    o, i = map(int, input().split())
    result -= o
    result += i
    max_r = max(max_r, result)
print(max_r)