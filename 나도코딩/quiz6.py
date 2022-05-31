# 표준 체중을 구하는 프로그램 작성

import sys

def std_weight(height, gender):
    s = 21 # 기본값 여자
    if gender == "남자":
        s = 22 # 남자일 경우
    weight = height * height * s
    return weight # 표준체중 출력
    
h, g = map(str, sys.stdin.readline().strip().split())
w = std_weight(int(h)/100, g)
print("키 {}cm {}의 표준 체중은 {:.2f}kg 입니다.".format(h, g, float(w)))