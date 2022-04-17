#3과 5의 배수의 합을 구하라
result = sum(list(filter(lambda x: not(x % 3) or not(x % 5), range(1, 1000))))
print(result)