# 파일 열기 / 모드 w: 새로 쓰기 모드, a: 뒤에 이어서 쓰기 모드, r: 읽기 모드 
file = open("chap05\\sec03\\basic.txt", "w") #파일경로, 모드 / 둘다 문자열

# 파일에 텍스트 작성
file.write("Hello Python Programming...!")

# 파일 닫기
file.close()


#with문 / 자동으로 파일이 열고 닫힘
with open("chap05\\sec03\\with.txt", "w") as file1:
    file1.write("Hello, This file was created as with")

# 파일 읽기 모드
with open("chap05\\sec03\\with.txt", "r") as file2:
    # 파일을 읽고 출력
    contents = file2.read()
print(contents)