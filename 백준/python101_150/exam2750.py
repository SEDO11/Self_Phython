# 수 정렬 하기

n = int(input())
list_n = []
for i in range(n):
    list_n.append(int(input()))
list_n.sort()
for i in list_n:
    print(i)