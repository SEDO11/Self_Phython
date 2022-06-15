# 수들의 합, 값이 입력될때 해당값을 만드는 수의 최댓값 출력

result = int(input())
num = 0
sum_result = 0

while True:
    if sum_result > result: # 더 한 값이 입력한 값보다 큰 경우
        num -= 1 # 감소
        print(num)
        break #종료
    else :
        num += 1 # 증가
        sum_result += num # 수들의 합