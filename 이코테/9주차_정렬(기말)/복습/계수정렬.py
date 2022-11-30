array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
result = [0] * (max(array)+1)

for i in array:
    result[i] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i, end=' ')