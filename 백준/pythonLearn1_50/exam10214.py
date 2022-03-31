#야구 연고전

run = int(input())
score_y = 0 #연세대 점수 변수
score_k = 0 # 고려대 점수 변수
for i in range(run): # 테스트 케이스 호출 횟수
    for j in range(9): # 테스트 케이스 9줄
        list_yk = input().split()
        y = int(list_yk[0])
        k = int(list_yk[1])
        score_y += y
        score_k += k
        
    if score_y > score_k: # 연세대가 이긴경우
        print("Yonsei")
    elif score_y < score_k: #고려대가 이긴경우
        print("Korea")
    else : # 비긴경우
        print("Draw")
    