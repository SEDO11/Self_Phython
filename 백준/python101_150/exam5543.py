#상근날드

b, w = [], []
for i in range(5):
    a = int(input())
    if i < 3:
        b.append(a)
    else:
        w.append(a)
r1 = min(b)
r2 = min(w)
print(r1+r2-50)