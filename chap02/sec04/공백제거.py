from pickletools import string4
import string


string1 = """
        안녕하세요
문자열 함수를 알아봅니다
"""
string2 = string1.strip() #공백 제거
string3 = string1.lstrip() #왼쪽 공백 제거
string4 = string1.rstrip() # 오른쪽 공백 제거

print(string1)
print(string2)
print(string3)
print(string4)