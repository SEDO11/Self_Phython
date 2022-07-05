#카이사르 암호를 영어로 전환

s = input()
r = ""
for i in s:
    if 68<= ord(i) <= 90:
        r += chr(ord(i)-3)
    else:
        r += chr(ord(i)+23)
print(r)
        