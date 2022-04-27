# 예외 구분

list_n = [52, 273, 32, 72, 100]

try:
    n = int(input("입력> "))
    print("{}번째 요소: {}".format(n, list_n[n]))
except ValueError:
    # ValueError가 발생한 경우
    print("정수를 입력해주세요.")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")
finally:
    print("종료")