#콘테스트

a = []
b = []
for i in range(20):
    if i < 10:
        a.append(int(input()))
    else:
        b.append(int(input()))
a.sort(reverse=True)
b.sort(reverse=True)
w = a[0] + a[1] + a[2]
k = b[0] + b[1] + b[2]
print(w, k)
