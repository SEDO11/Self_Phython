string = input()
num = int(string)

for i in range(num):
    a = input().split(" ")
    num_a0 = int(a[0])
    num_a1 = int(a[1])
    result = num_a0 + num_a1
    print(result)