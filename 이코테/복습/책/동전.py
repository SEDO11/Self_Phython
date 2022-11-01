#동전

m = [500, 100, 50, 10]
n = int(input())
cnt = 0
for i in m:
    cnt += n // i
    n %= i
print(cnt)