dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 키 접근
key = input("접근할 키를 입력하세요> ")
value = dictionary.get(key)
print("값: ", value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")