# 수 찾기

def fn(a, ma, s, e):
    if s > e:
        return 0
    m = (s+e)//2
    if a[m] > ma:
        return fn(a, ma, s, m-1)
    elif a[m] < ma:
        return fn(a, ma, m+1, e)
    else:
        return 1

n = int(input())
a = list(map(int, input().split()))
mn = int(input())
ma = list(map(int, input().split()))
a.sort()

for i in ma:
    print(fn(a, i, 0, n-1))