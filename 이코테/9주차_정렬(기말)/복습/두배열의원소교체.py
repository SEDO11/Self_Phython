# 두 배열의 원소 교체

n, k = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort(reverse=True)

for i in range(k):
    a[i], b[i] = b[i], a[i]
print(sum(a))