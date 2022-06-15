# 개표

while True:
    count_a = 0 # a 카운트 변수
    count_b = 0 # b 카운트 변수
    lenth = int(input()) # 범위 지정
    string = input() # 개표 입력
    
    if len(string) > lenth: # 범위가 초과 될 경우
        continue # 다시 입력
    list_s = list(string) # 리스트에 개표 값을 하나씩 대입
    
    for i in list_s: # a, b 카운트
        if i == "A":
            count_a += 1
        else :
            count_b += 1
            
    if count_a > count_b: # 출력, a > b 인 경우
        print("A")
    elif count_a < count_b: # 출력, a < b 인 경우
        print("B")
    else:
        print("Tie") # 출력, a == b 인 경우
    break