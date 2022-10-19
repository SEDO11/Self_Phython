numbers = [103, 52, 273, 32, 77]
list_a = reversed(numbers)

# 리스트 내부의 값이 숫자일 경우에만 사용 가능
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()

print(numbers)
print(list_a)
print(list(list_a))
print(numbers[::-1]) # 이것도 뒤집기 가능, 비 파괴적
print()

for i in reversed(numbers):
    print("-", i)