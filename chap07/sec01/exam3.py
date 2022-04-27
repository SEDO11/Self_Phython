# 현재 디렉토리를 읽어 들이고 파일인지 디렉토리인지 구분하기
#모듈을 읽어 들입니다.
import os

# 현재 폴더의 파일/ 폴더를 출력
out = os.listdir(".")
print(out)
print()

# 현재 폴더의 파일/ 폴더를 구분
print("# 폴더와 파일 구분")
for path in out:
    if os.path.isdir(path):
        print("폴더: " + path)
    else :
        print("파일: " + path)