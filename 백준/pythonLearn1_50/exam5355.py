#화성 수학
#@는 *3 / %는 +5 / #은 -7

run = int(input()) # 실행 횟수 입력
res = [] #출력 값 저장할 리스트 전역 변수 설정

for i in range(run): # 입력
    mars = input().split() #공백을 기준으로 입력값 분류
    result = 0
    for j in range(len(mars)): # 리스트 크기만큼 실행
        if mars[j] == "@": # @일 경우
            result *= 3
        elif mars[j] == "%": # %일 경우
            result += 5
        elif mars[j] == "#": # #일 경우
            result -= 7
        else: # 숫자인 경우
            result += float(mars[j])
    res.append(result) # 리스트에 결과값 저장

for i in range(run): # 결과 출력
    print("{:.2f}".format(res[i]))