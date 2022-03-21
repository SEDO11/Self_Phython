def sum_all(start=0, end=100, step=1):
    result = 0
    for i in range(start, end+1, step):
        result += i
    return result

print(sum_all(0, 100, 10))
print(sum_all(end=1000))
print(sum_all())
print(sum_all(end=100, step=2))