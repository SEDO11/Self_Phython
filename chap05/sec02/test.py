#최대 재귀 호출 제한 오류로 인해 넣어준 코드
# import sys
# sys.setrecursionlimit(10**6)

counter = 0
def rabbit(n):
    global counter # 함수 내에서 전역 변수를 사용할 경우 global을 써줘야 한다.
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return rabbit(n-1) + rabbit(n -2)
    
    
# print(rabbit(1))
# print(rabbit(2))
# print(rabbit(3))
# print(rabbit(4))
# print(rabbit(5))
# print(rabbit(6))
# print(rabbit(7))
print(rabbit(10)) #수열 값 출력
print(counter) # 계산 횟수