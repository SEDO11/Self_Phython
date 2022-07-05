#영수증

r = int(input())
t = int(input())
k = 0
for _ in range(t):
    a, b = map(int, input().split())
    k += a * b
print("Yes" if r == k else "No")