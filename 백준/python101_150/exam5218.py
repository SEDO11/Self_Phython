#알파벳 거리
n = int(input())
for _ in range(n):
    a, b = map(str, input().split())
    r = "Distances: "
    for i in range(len(a)):
        if ord(a[i]) <= ord(b[i]):
            r += str(ord(b[i]) - ord(a[i])) + " "
        elif ord(a[i]) > ord(b[i]):
            r += str(ord(b[i])+26 - ord(a[i])) + " "
    print(r)
