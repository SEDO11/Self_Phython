# 나는 요리사다

list_a = []
max_v = 0
max_i = 0
for i in range(5):
    list_a.append(list(map(int, input().split())))
    if max_v < sum(list_a[i]):
        max_i = i+1
        max_v = sum(list_a[i])
print(max_i, max_v)