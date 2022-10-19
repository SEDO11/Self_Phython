#예외 처리
numbers = [52, 273, 32, 103, 90, 10, 275]
num = input()
try:
    num = int(num)
    print("{} 가 내부에 들어있는지 확인".format(num))
    
    # 입력 된 값이 list 안에 없으면 여기에서 예외 발생
    print("{}는 {} 위치에 있습니다.".format(num, numbers.index(num)))
except:
    print("리스트 내부에 해당 값이 없습니다.")

