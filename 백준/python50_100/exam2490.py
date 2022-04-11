# 윷놀이
import sys
input = sys.stdin.readline

for _ in range(3):
    list_y = list(map(int, input().split()))
    result = list_y.count(0) #0의 개수 세기
    if result == 1: 
        print("A") #도
    elif result == 2:
        print("B") #개
    elif result == 3:
        print("C") #걸
    elif result == 4:
        print("D") #윷
    else:
        print("E") #모