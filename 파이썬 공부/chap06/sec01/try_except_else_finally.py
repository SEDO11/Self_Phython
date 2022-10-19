try:
    num = int(input("정수 입력> "))
    print("원의 반지름", num)
    print("원의 둘레", 2 * 3.14 * num)
    print("원의 넓이", 3.14 * num**2)
except:
    print("예외 발생, 정수가 아닙니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("프로그램을 종료합니다.")