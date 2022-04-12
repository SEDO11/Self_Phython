# num = int(input())
# print("원의 반지름", num)
# print("원의 둘레", 2 * 3.14 * num)
# print("원의 넓이", 3.14 * num**2)


# 위의 것은 정수가 입력되지 않으면 예외가 발생 되므로
# 밑의 코드를 통해 정수인지 확인하고 변환해서 출력
num = input()

if num.isdigit(): #입력된 값이 숫자 인지 확인
    num = int(num)
    
    print("원의 반지름", num)
    print("원의 둘레", 2 * 3.14 * num)
    print("원의 넓이", 3.14 * num**2)
else:
    print("정수가 아닙니다.")