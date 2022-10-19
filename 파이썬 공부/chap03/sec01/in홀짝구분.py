number = input()
last_character = number[-1] #맨 뒤의 숫자를 슬라이싱

if last_character in "02468": #in을 통해 맨 뒷자리의 숫자가 02468중에서 속한게 있는지 확인
    print("짝수")
else:
    print("홀수")