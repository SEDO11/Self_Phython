# 올해의 술꾼

run1 = int(input())
for i in range(run1): # 테스트 케이스 호출 횟수
    run2 = int(input()) # 테스트 케이스 비교 학교 개수 입력
    result_score = 0 #최대로 마신 술
    result_str = "" # 학교 이름
    for j in range(run2):
        list_yk = input().split()
        name = str(list_yk[0])
        score = int(list_yk[1])
        if score > result_score:
            result_score = score
            result_str = name
        
    print(result_str)