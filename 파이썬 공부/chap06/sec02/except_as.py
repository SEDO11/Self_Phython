#예외 구문과 예외 객체

list_n = [52, 273, 32, 72, 100]

try:
    n = int(input())
    print("{}번째 요소: {}".format(n, list_n[n]))
except ValueError as exception:
    # ValueError가 발생한 경우
    print("정수를 입력해주세요.")
    print("exception: ",exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception: ",exception)
finally:
    print("종료")    