string = input()
num = int(string)
list_a = []

for i in range(num):
    list_a.append(int(input()))
print(min(list_a), max(list_a))