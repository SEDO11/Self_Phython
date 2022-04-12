def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문 실행")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문 실행")
    else:
        print("else 구문 실행")
    finally:
        print("finally 구문 실행")
    print("test() 함수의 마지막 줄")

test()