a = input()
b = input()

result1 = int(a) * int(b[2:]) #첫번째 숫자
result2 = int(a) * int(b[1:2]) #두번째 숫자
result3 = int(a) * int(b[:1]) #세 번째 숫자
result4 = int(a) * int(b)

print(result1)
print(result2)
print(result3)
print(result4)