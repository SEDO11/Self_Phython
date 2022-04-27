# 모듈을 읽어 들입니다.
from urllib import request

target = request.urlopen("https://naver.com")
output = target.read()

print(output)