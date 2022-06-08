#소수 구하기
a, b = map(int, input().split())
for j in range(a, b+1):
    t = 0
    for i in range(2, j):
        if j%i == 0: # 소수가 아닌경우
            t = 1
            break  
    if t == 0: # 소수인 경우
        print(j)