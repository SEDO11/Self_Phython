# 수 찾기

run_a = int(input())
a = []
m = []
while True:
    a = list(map(int, input().split()))
    if len(list(a)) == run_a:
        break
    
run_m = int(input())
while True:
    m = list(map(int, input().split()))
    if len(list(a)) == run_m:
        break

for i in m:
    result = 1
    cnt = 0
    for j in a:
        if i == j:
            cnt += 1
    if cnt == 0:
        result = 0
    print(result)