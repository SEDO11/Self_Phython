number = input("정수 입력> ")
num = int(number)

if num > 0:
    print("양수 입니다. 값: {}".format(num))
    
if num < 0:
    print("음수 입니다. 값: {}".format(num))
    
if num == 0:
    print("0 입니다.")