#안테나

n = int(input())
l = list(map(int, input().split()))
l.sort()
k = ((n - 1)// 2)
print(l[k])