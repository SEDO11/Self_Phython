#대표값

list_a = []
cnt = 0
result = 0
for _ in range(10):
    list_a.append(int(input()))
for i in range(10):
    if cnt < list_a.count(list_a[i]):
        cnt = list_a.count(list_a[i])
        result = list_a[i]
print(sum(list_a)//10)
print(result)