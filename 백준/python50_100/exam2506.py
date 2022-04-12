#점수 계산

n = int(input())
list_n = list(map(int, input().split()))
cnt = 0
result = 0
for i in list_n:
    if i == 1: 
        result += i + cnt 
        cnt += 1
    else : cnt = 0
print(result)