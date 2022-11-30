l = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(l)):
    min_index = i
    for j in range(i+1, len(l)):
        if l[min_index] > l[j]:
            min_index = j
    l[min_index], l[i] = l[i], l[min_index]
print(list(l))