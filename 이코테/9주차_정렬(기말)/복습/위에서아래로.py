#위에서 아래로

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
print(list(arr))