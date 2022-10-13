#문자열 압축

def fn(s):
    m = 1000
    for i in range(1, len(s)):
        x = s[:i]
        r = ''
        tmp = 1
        for j in range(i, len(s)+i, i):
            if s[j:j+i] == x:
                tmp += 1
            else:
                if tmp > 1:
                    r += str(tmp) + x
                else:
                    r += x
                tmp = 1
                x = s[j:j+i]
        m = min(len(r), m)
    return m

s = input()
print(fn(s))
