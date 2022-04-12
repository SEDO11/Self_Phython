# 차량 10부제

d = int(input())
list_d = list(map(int, input().split()))
result = 0
for i in list_d:
    if i == d:
        result += 1
print(result)