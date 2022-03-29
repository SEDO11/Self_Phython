# 문자열 반복

run = int(input())

for i in range(run):
    test = input().split()
    num = int(test[0])
    string = test[1]
    result = ""
    for j in range(len(string)):
        result += string[j] * num
    print(result)