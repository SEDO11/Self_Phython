import re


def sum_all(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
    return result

print("0~100:",sum_all(0, 100))
print("0~1000:",sum_all(0, 1000))
print("50~100:",sum_all(50, 100))
print("500~1000:",sum_all(500, 1000))