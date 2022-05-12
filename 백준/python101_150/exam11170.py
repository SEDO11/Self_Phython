#0의 개수

n = int(input())
for _ in range(n):
    s = ""
    a, b = map(int, input().split())
    for i in range(a, b+1):
        s += str(i)
    print(s.count('0'))