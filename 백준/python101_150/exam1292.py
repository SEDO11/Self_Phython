# 쉽게 푸는 문제

list_n = []
j, i, result = 1, 0, 0
while i < 1000: # 수열 1000개 생성
    for _ in range(j):
        list_n.append(j)
        i+=1
    j+=1
a, b = map(int, input().split())
for i in list_n[a-1:b]:
    result += i
print(result)