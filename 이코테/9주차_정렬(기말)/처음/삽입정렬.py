#삽입정렬

l = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        d = l[i+1]
        for j in range(i+1):
            if l[j] > d:
                l.remove(d)
                l.insert(j, d)
                break
for i in l:
    print(i)