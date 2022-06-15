#약수들의 합

while True:
    
    num = int(input())
    cnt1 = 0
    cnt1_str = "" # 합 저장 문자열
    result = "" # 최종 문자열
    if num > 0: # 양수일 경우 실행
        for i in range(1, num): # 자신을 제외 한 수
            if num % i == 0:
                cnt1 += i
                if i == 1:
                    cnt1_str += " = " + str(i)
                else :
                    cnt1_str += " + " + str(i)
    else : #음수일 경우 종료
        break
        
    if num == cnt1: # 완전수일 경우
        result = str(num) + cnt1_str
        print(result)
    else :  # 완전수가 아닌 경우
        result = str(num) + " is NOT perfect."
        print(result)