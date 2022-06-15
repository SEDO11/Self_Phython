string = input()
num = int(string)

for i in range(1, num+1):
    result = ""
    for j in range(num, 0, -1):
        if i < j:
            result += " "
        else:
            result += "*"
    print(result)