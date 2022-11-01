#전화번호문자조합

import itertools

phone = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], 
     ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
     ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

l = []
lst = list(map(int, input()))
for i in lst:
    l.append(phone[i])
pro = list(itertools.product(*l))

print([''.join(i) for i in pro])
