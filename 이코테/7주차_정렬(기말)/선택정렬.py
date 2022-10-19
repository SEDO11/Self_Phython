
l = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
g = []

for i in range(len(l)-1):
    g = i
    for j in range(i+1, len(l)):
        if l[g] > l[j]:
            g = j
    l[i], l[g] = l[g], l[i]
print(list(l))