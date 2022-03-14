list_a = [273, 32, 103, "문자열", True, False]
list_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 범위 지정 출력
print(list_a[3])
print(list_a[3][2])
print(list_a[3][0:2])
print()
print(list_b[1])
print(list_b[1][1])

# 기존 리스트에 값 추가
list_a.append("오세훈")
list_a.insert(0, "안녕하세요")
list_a.insert(3, "곤니찌와")
print(list_a)
print()
list_a.extend([4, 5, 6, 7])
print(list_a)
list_a.extend(list_b)
print()
print(list_a)

list_a.pop(3)
print(list_a)