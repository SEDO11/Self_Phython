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
    if type(character[key]) == str:
        print(key, ":", character[key])
    elif type(character[key]) == int:
        print(key, ":", character[key])
    elif type(character[key]) == dict:
        for key1 in character[key]:
            print(key1, ":", character[key][key1])
    else:
        for key1 in character[key]:
            print(key, ":", key1)