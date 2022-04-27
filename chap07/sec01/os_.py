# os 모듈

from os import *

# 기본 정보 출력
# print(name) # 운영 체제
# print(getcwd()) # 현재 폴더
# print(listdir()) # 폴더 내부 요소

#폴더를 만들고 제거
# mkdir("hello") # 만들기
# rmdir("hello") # 제거

# 파일을 생성하고 파일 이름 변경
try:
    with open("original.txt", "w") as file:
        file.write(1)
    rename("original.txt", "new.txt")
except:
    print("오류발생")

# 파일 제거
# remove("new.txt")

# 시스템 명령어, cmd에서 dir 입력 했을 때와 똑같음
system("dir")