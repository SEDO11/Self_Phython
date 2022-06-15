a = input()
b = input()

result1 = int(a) * int(b[2:]) # 일의 자리 수
result2 = int(a) * int(b[1:2]) # 십의 자리 수
result3 = int(a) * int(b[:1]) # 백의 자리 수
result4 = int(a) * int(b)

print(result1)
print(result2)
print(result3)
print(result4)