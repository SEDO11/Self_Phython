#아름다운 수

t = int(input())
for _ in range(t):
    l = []
    n = int(input())
    cnt = 0
    
    while n > 0:
        k = n % 10
        if k not in l:
            l.append(k)
            cnt += 1
        n = n // 10
    print(cnt)
