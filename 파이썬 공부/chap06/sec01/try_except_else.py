# else는 굳이 안써도 되지만 알아두라
try:
    num = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름", num)
    print("원의 둘레", 2 * 3.14 * num)
    print("원의 넓이", 3.14 * num**2)