character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀 플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str: # 문자열 일 때 
        print(key, ":", character[key])
    elif type(character[key]) is list: # 리스트 일 때
        for key1 in character[key]:
            print(key, ":", key1)
    elif type(character[key]) is dict: # 딕셔너리 일 때
        for key1 in character[key]:
            print(key1, ":", character[key][key1])
    else: # 실수 일 때
        print(key, ":", character[key])