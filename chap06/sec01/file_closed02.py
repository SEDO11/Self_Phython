# finally를 사용하지 않으면 실행이 제대로 안되는 현상 발생
try:
    file = open("info.txt", "w") #파일 열기
    예외.발생()
    file.close() #파일 닫기
except Exception as e:
    print(e)
print("파일이 닫혔는가?> ", file.closed)