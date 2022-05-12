#ROT13

s = input()
r = ""
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90: # A~Z 사이일때
        n = ord(s[i]) + 13
        if 65 <= n <= 90:
            r += chr(n)
        else:
            n = 65 + 12 - 90 + ord(s[i])
            r += chr(n)
    elif 97 <= ord(s[i]) <= 122: # A~Z 사이일때
        n = ord(s[i]) + 13
        if 97 <= n <= 122:
            r += chr(n)
        else:
            n = 97 + 12 - 122 + ord(s[i])
            r += chr(n)
    else: # 공백, 숫자
        r += s[i]
print(r)