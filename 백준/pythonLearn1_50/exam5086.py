# 배수와 약수
# 1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

while True:
    list_a = input().split()
    a = int(list_a[0])
    b = int(list_a[1])
    
    if a < b:
        if b % a == 0: # 약수 인 경우
            print("factor")
        else :
            print("neither")
    elif a > b:
        if a % b == 0: # 배수 인 경우
            print("multiple")
        else :
            print("neither")
    elif a == 0 and b == 0: # 0 0 이면 종료
        break
    else :
        print("neither")