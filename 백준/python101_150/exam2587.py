#대표값2

list_a = []
for i in range(5):
    list_a.append(int(input()))
list_a.sort()
print(sum(list_a)//5)
print(list_a[2])