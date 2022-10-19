list_n = [52, 273, 32, 72, 100]

try:
    n = int(input())
    print("{}번째 요소: {}".format(n, list_n[n]))
    # 예외
except ValueError as exception:
    # ValueError 예외가 발생한 경우
    print("정수를 입력해주세요.")
    print("exception: ",exception)
except IndexError as exception:
    # IndexError 예외가 발생한 경우
    print("리스트의 인덱스를 벗어났어요!")
    print("exception: ",exception)
except Exception as exception:
    # 이외의 예외가 발생한 경우
    print("파악하지 못 한 예외가 발생했습니다.")
    print("exception: ",exception)
finally:
    print("종료")   