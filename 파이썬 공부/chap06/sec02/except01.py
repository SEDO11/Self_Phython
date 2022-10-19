# 예외 객체를 통한 예외 처리
import math

PI = math.pi
try:
    #숫자 변환
    a = int(input("입력> "))
    print("반지름", a)
    print("둘레 {:.2f}".format(2 * PI * a))
    print("원의 넓이 {:.2f}".format(PI * a ** 2))
except Exception as exception: # 예외 객체
    print("type*exception): ", type(exception))
    print("exception: ", exception)