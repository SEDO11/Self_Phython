
n = input()
number = 0
s_cnt = 0
s = []
s_sum = []
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
s_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in n:
    if i.isdigit():
        number += int(i)
    else:
        s.append(i)
        
for i in s:
    s_sum.append(l[ord(i)-97])
for i in s_list:
    s_cnt = max(s_cnt, s.count(i))
    
s_sum = sum(s_sum) % 26
number %= 26
s_cnt %= 26

print(str(s_sum) + (str(number) if number > 9 else '0'+str(number))  +(str(s_cnt) if s_cnt > 9 else '0'+str(s_cnt)))