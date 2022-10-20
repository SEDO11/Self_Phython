#볼링공고르기

n, m = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if l[i] != l[j]:
            cnt += 1
print(cnt)