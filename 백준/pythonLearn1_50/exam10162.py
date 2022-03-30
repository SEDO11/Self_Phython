# 전자 레인지

a = 300 # 5분
b = 60 # 1분
c = 10 # 10초
result_a = 0 # 버튼 누른 횟수 저장 변수
result_b = 0 # 버튼 누른 횟수 저장 변수
result_c = 0 # 버튼 누른 횟수 저장 변수

while True:
    num = int(input())
    if 1 <= num <= 10000: # 1이상 10000이하 일 경우 옳바른 범위 이므로 종료
        break 
    
temp = num # 초기에 입력된 시간 저장 변수

while True:
    if num >= a : # 5분 이상일 경우
        result_a = num // a 
        num %= a
    elif num >= b: # 1분 이상일 경우
        result_b = num // b
        num = num % b
    else : # 10초 이상일 경우
        result_c = num // c
        num %= c
        break # 10초 까지 연산하면 종료

if temp == (result_a * a) + (result_b * b) + (result_c * c): # 시간을 맞출 수 있는 경우
    print(result_a, result_b, result_c)
else : # 시간을 맞출 수 없는 경우
    print(-1)