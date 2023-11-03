#알파벳
s = input()
s_num = 0
n = 0
cnt = 0

for i in s:
    if i.isdigit():
        n += int(i)
    else:
        s_num += ord(i) - 97
        
for i in range(97, 123):
    if cnt < s.count(chr(i)):
        cnt = s.count(chr(i))
        
s_num %= 26
n %= 26
cnt %= 26

s_num = str(s_num) if  s_num > 9 else '0' + str(s_num)
n = str(n) if  n > 9 else '0' + str(n)
cnt = str(cnt) if  cnt > 9 else '0' + str(cnt)
print(s_num+n+cnt)