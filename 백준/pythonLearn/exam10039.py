#평균 점수

sumit = 0 #

for i in range(5):
    num = int(input())
    if num < 40: #40 미만인 경우 40을 더함
        sumit += 40
    else : # 아닌경우 해당 점수를 더함
        sumit += num
    
avg = sumit // 5 # 정수형 나눗셈후 평균 값에 대입
print(avg)