dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print(dictionary)
print()
# 출력합니다.
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("ingredient:", dictionary["ingredient"][3])
print("origin:", dictionary["origin"])
print()

# 값을 변경합니다.
dictionary["name"] = "8D 건조 망고"

# 새로운 자료 추가
dictionary["price"] = 5000
print(dictionary)
print()

# 자료 삭제
del dictionary["ingredient"]
print(dictionary)
print()