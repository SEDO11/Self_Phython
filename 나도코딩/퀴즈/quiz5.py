# 50명의 승객과 매칭
from random import *
cnt = 0 # 총 승객 탑승 수 
for i in range(1, 51): # 50번 반복
    num = randrange(5, 51) # 5~50분 난수 발생
    c = " " # 매칭이 아닐경우 공백
    if 5 <= num <= 15: # 5~15분 손님 매칭
        c = "o" # 매칭될 경우 o 표시
        cnt += 1 # 탑승 승객 증가
    print("[{}] {}번째 손님 (소요시간: {}분)".format(c, i, num))
print("총 탑승 승객 : {} 분".format(cnt))