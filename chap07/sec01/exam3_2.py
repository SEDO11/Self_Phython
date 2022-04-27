# 재귀 함수를 통해 현재 폴더 내부에 있는 모든 파일을 탐색
import os

# 현재 폴더의 파일/ 폴더를 출력
out = os.listdir(".")
print(out)
print()

# 현재 폴더의 파일/ 폴더를 구분
print("# 폴더와 파일 구분")
def der(path):
    out = os.listdir(path)
    for item in out:
        if os.path.isdir(path+"/"+item):
            print(path+"/"+item)
            der(path+"/"+item)
        else :
            print("파일: " + item)
            
der(".")