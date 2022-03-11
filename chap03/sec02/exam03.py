str_input = input("태어난 해를 입력해 주세요.> ")
birth_year = int(str_input) % 12

if birth_year == 0:
    print("원숭이")
elif birth_year == 1:
    print("닭")
elif birth_year == 2:
    print("개")
elif birth_year == 3:
    print("돼지")
elif birth_year == 4:
    print("쥐")
elif birth_year == 5:
    print("소")
elif birth_year == 6:
    print("범")
elif birth_year == 7:
    print("토끼")
elif birth_year == 8:
    print("용")
elif birth_year == 9:
    print("뱀")
elif birth_year == 10:
    print("말")
else:
    print("양")