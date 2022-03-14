# 리스트의 위치를 지정한 제거
list_a = [0, 1, 2, 3, 4, 5]
print("제거")

del list_a[1]
print(list_a)

list_a.pop(2)
print(list_a)

# 리스트 내부의 동일한 값 제거
list_b = [1, 2, 1, 2]
list_b.remove(2)
print(list_b)

# 리스트 내의 자료 모두 제거
list_a.clear()
print(list_a)