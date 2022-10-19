while True:
    try:
        print("try 구문 실행")
        break
    except:
        print("except 구문 실행")
    finally:
        print("finally 구문 실행")
print("종료")