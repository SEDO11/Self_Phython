#삽입정렬

import time

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = []

# 내 풀이
for i in array:
    if len(result) == 0:
        result.append(i)
        continue
    
    for j in range(len(result)+1):
        if j == len(result):
            result.insert(j, i)
            break
        
        if result[j] > i:
            result.insert(j, i)
            break
print(list(result))

# 책 풀이
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break
print(list(array))