# try except를 이용한 예외 처리
try:
    # 숫자로 변환
    num = int(input("정수입력> "))
    print("원의 반지름", num)
    print("원의 둘레", 2 * 3.14 * num)
    print("원의 넓이", 3.14 * num**2)
except:
    print("무언가 잘못 되었습니다.")